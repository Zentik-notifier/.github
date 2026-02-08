from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageOps

TARGETS = [
    (2064, 2752),
    (2752, 2064),
    (2048, 2732),
    (2732, 2048),
]


def choose_nearest_target(width: int, height: int) -> tuple[int, int]:
    # Choose target minimizing relative aspect mismatch first, then relative pixel distance.
    src_ar = width / height

    def score(t: tuple[int, int]) -> tuple[float, float]:
        tw, th = t
        tar_ar = tw / th
        ar_mismatch = abs(math.log(src_ar / tar_ar))
        # relative euclidean distance in pixel space
        dw = (width - tw) / tw
        dh = (height - th) / th
        pix_dist = math.hypot(dw, dh)
        return (ar_mismatch, pix_dist)

    return min(TARGETS, key=score)


def convert_to_srgb_rgb(img: Image.Image) -> Image.Image:
    # Ensure no alpha and RGB output for App Store Connect.
    if img.mode in ("RGBA", "LA"):
        # Composite on white to remove alpha.
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.getchannel("A"))
        return background

    if img.mode == "P":
        img = img.convert("RGBA")
        return convert_to_srgb_rgb(img)

    if img.mode != "RGB":
        img = img.convert("RGB")

    return img


def resize_fit_width_no_horizontal_crop(
    img: Image.Image,
    target_w: int,
    target_h: int,
    *,
    pad_color: tuple[int, int, int] = (255, 255, 255),
) -> Image.Image:
    """Resize to exactly target size without ever cropping left/right.

    Strategy:
    - Always scale to match target width.
    - If height is larger: center-crop top/bottom.
    - If height is smaller: pad top/bottom (letterbox) to reach exact height.
    """

    src_w, src_h = img.size
    scale = target_w / src_w
    new_w = target_w
    new_h = int(round(src_h * scale))

    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

    if new_h == target_h:
        return resized

    if new_h > target_h:
        top = (new_h - target_h) // 2
        return resized.crop((0, top, target_w, top + target_h))

    # new_h < target_h: pad vertically
    canvas = Image.new("RGB", (target_w, target_h), pad_color)
    top = (target_h - new_h) // 2
    canvas.paste(resized, (0, top))
    return canvas


def main() -> int:
    parser = argparse.ArgumentParser(description="Resize screenshots to nearest App Store Connect iPad sizes")
    parser.add_argument("--in-dir", default=".", help="Input directory containing images")
    parser.add_argument("--out-dir", default="resized", help="Output directory")
    parser.add_argument("--quality", type=int, default=95, help="JPEG quality (1-100)")
    args = parser.parse_args()

    in_dir = Path(args.in_dir).expanduser().resolve()
    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    exts = {".png", ".jpg", ".jpeg"}
    inputs = sorted([p for p in in_dir.iterdir() if p.is_file() and p.suffix.lower() in exts])

    if not inputs:
        print(f"No images found in {in_dir}")
        return 1

    print(f"Found {len(inputs)} image(s) in {in_dir}")

    for path in inputs:
        with Image.open(path) as img:
            img = ImageOps.exif_transpose(img)
            img.load()
            w, h = img.size
            tw, th = choose_nearest_target(w, h)

            img_rgb = convert_to_srgb_rgb(img)
            out_img = resize_fit_width_no_horizontal_crop(img_rgb, tw, th)

            out_name = f"{path.stem}_{tw}x{th}.jpg"
            out_path = out_dir / out_name

            out_img.save(
                out_path,
                format="JPEG",
                quality=max(1, min(100, int(args.quality))),
                optimize=True,
                progressive=True,
            )

            print(f"{path.name}: {w}x{h} -> {tw}x{th} => {out_path.name}")

    print(f"Done. Output in: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
