"""Checks every number quoted in 'The Power of Colouring'. Run: python3 check_claims.py
No packages needed."""
from itertools import combinations
from math import comb, sqrt, cos, sin, pi, asin, hypot, floor
import random


def colour_counts(rows, cols, k, f):
    t = [0] * k
    for i in range(rows):
        for j in range(cols):
            t[f(i, j)] += 1
    return t


print("1. Strips of 4 on a 10 x 10 board")
print("   diagonals, 4 colours:", colour_counts(10, 10, 4, lambda i, j: (i + j) % 4))
print("   chessboard:          ", colour_counts(10, 10, 2, lambda i, j: (i + j) % 2))
print("   2 x 2 blocks:        ", colour_counts(10, 10, 2, lambda i, j: (i // 2 + j // 2) % 2))

print("2. Strip theorem: colours equal exactly when k divides a side (boards up to 12 x 12, k up to 6)")
bad = 0
for k in range(2, 7):
    for m in range(1, 13):
        for n in range(1, 13):
            t = colour_counts(m, n, k, lambda i, j: (i + j) % k)
            if (len(set(t)) == 1) != (m % k == 0 or n % k == 0):
                bad += 1
print("   exceptions found:", bad)


def clean_colourings(n):
    """Red/blue colourings of the links among n people with no one-colour triangle."""
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}
    tris = [(1 << idx[(a, b)]) | (1 << idx[(a, c)]) | (1 << idx[(b, c)]) for a, b, c in combinations(range(n), 3)]
    return sum(all((m & t) not in (0, t) for t in tris) for m in range(1 << len(edges))), 1 << len(edges)


print("3. Party problem")
for n in (5, 6):
    clean, total = clean_colourings(n)
    print(f"   {n} people: {clean} of {total} colourings avoid a one-colour triangle")

print("4. Coin-flip colourings: average number of one-colour groups")
for n, k in ((6, 4), (1000, 20)):
    print(f"   {n} people, groups of {k}: {comb(n, k) * 2 ** (1 - comb(k, 2)):.3g}")
print("   groups of 20 among 1000 people: a", len(str(comb(1000, 20))), "digit number")
print("   2^903 has", len(str(2 ** 903)), "digits")

print("5. Final puzzle: 8 x 8 board, one square removed, strips of 3")
print("   colours, one diagonal direction:", colour_counts(8, 8, 3, lambda i, j: (i + j) % 3))
print("   colours, the other direction:   ", colour_counts(8, 8, 3, lambda i, j: (i - j) % 3))


def tileable(hole):
    g = [[False] * 8 for _ in range(8)]
    g[hole[0]][hole[1]] = True

    def rec():
        for r in range(8):
            for c in range(8):
                if not g[r][c]:
                    if c + 2 < 8 and not g[r][c + 1] and not g[r][c + 2]:
                        g[r][c] = g[r][c + 1] = g[r][c + 2] = True
                        if rec():
                            return True
                        g[r][c] = g[r][c + 1] = g[r][c + 2] = False
                    if r + 2 < 8 and not g[r + 1][c] and not g[r + 2][c]:
                        g[r][c] = g[r + 1][c] = g[r + 2][c] = True
                        if rec():
                            return True
                        g[r][c] = g[r + 1][c] = g[r + 2][c] = False
                    return False
        return True
    return rec()


print("   squares whose removal allows a tiling (row, column from 1):",
      [(r + 1, c + 1) for r in range(8) for c in range(8) if tileable((r, c))])

print("6. Seven colours for the plane (hexagons 0.9 across)")
R = 0.45


def hex_colour(x, y):
    q, r = (sqrt(3) / 3 * x - y / 3) / R, (2 / 3 * y) / R
    z = -q - r
    rq, rr, rz = round(q), round(r), round(z)
    dq, dr, dz = abs(rq - q), abs(rr - r), abs(rz - z)
    if dq > dr and dq > dz:
        rq = -rr - rz
    elif dr > dz:
        rr = -rq - rz
    return (rq - 2 * rr) % 7


random.seed(1)
clashes = 0
for _ in range(500_000):
    x, y, a = random.uniform(-20, 20), random.uniform(-20, 20), random.uniform(0, 2 * pi)
    clashes += hex_colour(x, y) == hex_colour(x + cos(a), y + sin(a))
print("   same-colour pairs at distance 1 in 500,000 random tries:", clashes)

print("7. Moser spindle")
rot = lambda p, t: (p[0] * cos(t) - p[1] * sin(t), p[0] * sin(t) + p[1] * cos(t))
phi = 2 * asin(1 / (2 * sqrt(3)))
B, C = rot((1, 0), 0), rot((1, 0), pi / 3)
D = (B[0] + C[0], B[1] + C[1])
P = [(0, 0), B, C, D, rot(B, phi), rot(C, phi), rot(D, phi)]
E = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (0, 4), (0, 5), (4, 5), (4, 6), (5, 6), (3, 6)]
print("   link lengths:", sorted({round(hypot(P[a][0] - P[b][0], P[a][1] - P[b][1]), 6) for a, b in E}))


def colourable(k):
    def rec(v, col):
        if v == 7:
            return True
        return any(all(col[u] != c for u in range(v) if (u, v) in E or (v, u) in E) and rec(v + 1, col + [c]) for c in range(k))
    return rec(0, [])


print("   3 colours enough:", colourable(3), " 4 colours enough:", colourable(4))
