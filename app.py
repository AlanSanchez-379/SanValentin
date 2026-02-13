import math
from flask import Flask, render_template_string, request

app = Flask(__name__)


def heart_points(scale=14, steps=800):
    pts = []
    for i in range(steps + 1):
        t = i * 2 * math.pi / steps
        x = 16 * math.sin(t) ** 3 * scale
        y = (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)) * scale / 13
        pts.append((x, y))
    return pts


def svg_path_from_points(pts, width=900, height=750):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    minx, miny, maxx, maxy = min(xs), min(ys), max(xs), max(ys)
    w = maxx - minx if maxx > minx else 1
    h = maxy - miny if maxy > miny else 1
    scale_x = (width * 0.7) / w
    scale_y = (height * 0.7) / h
    s = min(scale_x, scale_y)
    cx = width / 2
    cy = height / 2
    parts = []
    for i, (x, y) in enumerate(pts):
        sx = cx + x * s
        sy = cy - y * s
        if i == 0:
            parts.append(f"M {sx:.2f} {sy:.2f}")
        else:
            parts.append(f"L {sx:.2f} {sy:.2f}")
    parts.append("Z")
    return " ".join(parts)


HTML = '''<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>Corazón</title>
    <style>
      body { background:#0b0b0b; color:#fff; font-family:Arial, sans-serif; display:flex; align-items:center; justify-content:center; height:100vh; margin:0 }
      .card { text-align:center }
      svg { max-width:90vw; max-height:90vh; display:block; margin:0 auto }
      .message { margin-top:12px; font-weight:bold }
    </style>
  </head>
  <body>
    <div class="card">
      <svg id="heart" width="900" height="750" viewBox="0 0 900 750" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Corazón">
        <path d="{{ path }}" fill="#ff3b3b" stroke="#ff7b7b" stroke-width="2"/>
      </svg>
      <div class="message">{{ message }}</div>
    </div>
  </body>
</html>
'''


@app.route('/')
def index():
    message = request.args.get('message', '¿Quieres ser mi San Valentín?')
    pts = heart_points(scale=14, steps=1000)
    path = svg_path_from_points(pts, width=900, height=750)
    return render_template_string(HTML, path=path, message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
