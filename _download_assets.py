#!/usr/bin/env python3
"""Download project page assets from GitHub / Obsidian notes."""
from __future__ import annotations

import base64
import json
import subprocess
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def gh_api(path: str) -> dict | list:
    out = subprocess.check_output(["gh", "api", path], text=True)
    return json.loads(out)


def download_url(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "portfolio-builder"})
    with urllib.request.urlopen(req) as resp:
        dest.write_bytes(resp.read())
    print(f"OK {dest.relative_to(ROOT)} ({dest.stat().st_size} bytes)")


def download_repo_file(repo: str, path: str, dest: Path) -> None:
    enc = urllib.parse.quote(path)
    data = gh_api(f"repos/Arno1235/{repo}/contents/{enc}")
    if isinstance(data, list):
        raise RuntimeError(f"expected file, got dir: {repo}/{path}")
    if data.get("download_url"):
        download_url(data["download_url"], dest)
    elif data.get("content"):
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(base64.b64decode(data["content"]))
        print(f"OK(b64) {dest.relative_to(ROOT)}")
    else:
        raise RuntimeError(f"no content for {repo}/{path}")


def download_obsidian(path: str, dest: Path) -> None:
    enc = urllib.parse.quote(path)
    data = gh_api(f"repos/Arno1235/obsidian_notes/contents/{enc}")
    download_url(data["download_url"], dest)


ASSETS = [
    ("repo", "takeout", "print-output/map-a3.png", "projects/takeout/assets/map.png"),
    ("repo", "takeout", "print-output/leaderboard.png", "projects/takeout/assets/leaderboard.png"),
    ("repo", "takeout", "print-output/resto-sprites.png", "projects/takeout/assets/resto-sprites.png"),
    ("repo", "takeout", "print-output/magnet-sprites.png", "projects/takeout/assets/magnet-sprites.png"),
    (
        "repo",
        "factory-os",
        "03-hub/01-v1b/design/uploads/draw-23870731-b1e3-4e45-a6ce-98547b4acc35.png",
        "projects/factory-os/assets/diagram-1.png",
    ),
    (
        "repo",
        "factory-os",
        "03-hub/01-v1b/design/uploads/draw-30327cc8-e89a-41a2-8e6f-7e637e39705b.png",
        "projects/factory-os/assets/diagram-2.png",
    ),
    (
        "repo",
        "factory-os",
        "03-hub/01-v1b/design/uploads/draw-446dac10-feec-45bf-86ef-b2349814e32d.png",
        "projects/factory-os/assets/diagram-3.png",
    ),
    (
        "repo",
        "factory-os",
        "03-hub/01-v1b/design/uploads/draw-8708b10d-bf09-4556-8d77-237823caf708.png",
        "projects/factory-os/assets/diagram-4.png",
    ),
    ("repo", "MVTec_YOLO", "images/val_batch0_pred.jpg", "projects/mvtec-yolo/assets/predictions.jpg"),
    ("repo", "YAMAL", "examples/nodes/imaging/image.png", "projects/yamal/assets/example.png"),
    ("repo", "FitnessApp", "Original Images/pic00.jpg", "projects/fitnessapp/assets/pic00.jpg"),
    ("repo", "FitnessApp", "Original Images/pic01.jpg", "projects/fitnessapp/assets/pic01.jpg"),
    ("repo", "FitnessApp", "Original Images/pic02.jpg", "projects/fitnessapp/assets/pic02.jpg"),
    ("repo", "FitnessApp", "Original Images/pic03.jpg", "projects/fitnessapp/assets/pic03.jpg"),
    (
        "repo",
        "CryptoAI",
        "test_results/test_01/Prediction_acc=0.8565.PNG",
        "projects/cryptoai/assets/prediction.png",
    ),
    ("repo", "CryptoAI", "test_results/test_01/Werkelijk.png", "projects/cryptoai/assets/actual.png"),
    ("repo", "McDo_FlappyWacko", "template1.png", "projects/mcdo-bots/assets/flappy-1.png"),
    ("repo", "McDo_FlappyWacko", "template2.png", "projects/mcdo-bots/assets/flappy-2.png"),
    ("repo", "McDo_CandyCrush", "test.png", "projects/mcdo-bots/assets/candy-test.png"),
    (
        "repo",
        "Volvo-Battery-Widget",
        "Volvo Battery Widget/NumberWidgetExtension/Assets.xcassets/car.imageset/car.png",
        "projects/volvo-widgets/assets/car.png",
    ),
    (
        "url",
        "https://user-images.githubusercontent.com/67476721/213893967-8e26913b-ad6f-4b09-bac9-73c4e8b65181.png",
        "projects/mcdo-bots/assets/candycrush.png",
    ),
    (
        "url",
        "https://user-images.githubusercontent.com/67476721/213892255-b44fd15d-b763-45a3-9e1e-589bc7c7e725.png",
        "projects/ble-notificator/assets/screen-1.png",
    ),
    (
        "url",
        "https://user-images.githubusercontent.com/67476721/213892325-87f8f10d-c420-447c-ad8c-9c12263b1473.png",
        "projects/ble-notificator/assets/screen-2.png",
    ),
    (
        "obs",
        "00 - projects/00 - personal/04 - PCB raspi drone/99 - assets/Screenshot 2024-11-13 at 14.30.34.png",
        "projects/pcb-drone/assets/screenshot.png",
    ),
    (
        "obs",
        "00 - projects/00 - personal/04 - PCB raspi drone/99 - assets/Pasted image 20250813175846.png",
        "projects/pcb-drone/assets/board.png",
    ),
    (
        "obs",
        "00 - projects/00 - personal/04 - PCB raspi drone/99 - assets/digikey-basket.png",
        "projects/pcb-drone/assets/digikey.png",
    ),
    (
        "obs",
        "00 - projects/00 - personal/05 - Market Ops/00 - planning/01 - reports/00 - assets/00 - diagram.png",
        "projects/market-ops/assets/diagram.png",
    ),
    (
        "obs",
        "00 - projects/00 - personal/05 - Market Ops/00 - planning/01 - reports/00 - assets/Screenshot 2025-07-22 at 22.34.44.png",
        "projects/market-ops/assets/screenshot.png",
    ),
]


def main() -> None:
    for item in ASSETS:
        kind = item[0]
        try:
            if kind == "repo":
                _, repo, path, dest = item
                download_repo_file(repo, path, ROOT / dest)
            elif kind == "url":
                _, url, dest = item
                download_url(url, ROOT / dest)
            elif kind == "obs":
                _, path, dest = item
                download_obsidian(path, ROOT / dest)
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL {item}: {exc}")


if __name__ == "__main__":
    main()
