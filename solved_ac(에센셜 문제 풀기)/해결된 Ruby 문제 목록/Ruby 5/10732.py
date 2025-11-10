# 10732번(소방차게임) 문제 : https://www.acmicpc.net/problem/10732
import sys
import math
import heapq
from bisect import bisect_right
from typing import List, Tuple, Dict, Any, Set

input = sys.stdin.readline

# 소방차는 빨간불에도 멈추지 않아! Boy❤️

INF = 1e100
EPS_DENOM = 1e-12
EPS_DISC = 1e-9

# 좌표 양자화 (1e-6 정밀도)
KEY_PREC_SCALE:int = 1e6

# ===== 기초 기하 =====

def ccw(ax: float, ay: float,
        bx: float, by: float,
        cx: float, cy: float) -> int:
    v:float = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
    if v > 0:
        return 1
    if v < 0:
        return -1
    return 0

def segments_intersect(s1: Tuple[float, float, float, float],
                       s2: Tuple[float, float, float, float]) -> bool:
    x1, y1, x2, y2 = s1
    x3, y3, x4, y4 = s2

    # bounding box 빠른 거절
    if (max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2) or
        max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2)):
        return False

    o1:int = ccw(x1, y1, x2, y2, x3, y3)
    o2:int = ccw(x1, y1, x2, y2, x4, y4)
    o3:int = ccw(x3, y3, x4, y4, x1, y1)
    o4:int = ccw(x3, y3, x4, y4, x2, y2)

    # 공선인 경우 : 투영 구간이 겹치면 교차
    if o1 == 0 and o2 == 0 and o3 == 0 and o4 == 0:
        if (max(min(x1, x2), min(x3, x4)) <= min(max(x1, x2), max(x3, x4)) and
            max(min(y1, y2), min(y3, y4)) <= min(max(y1, y2), max(y3, y4))):
            return True
        return False

    return (o1 * o2 <= 0 and o3 * o4 <= 0)

def intersection_params(s1: Tuple[float, float, float, float],
                        s2: Tuple[float, float, float, float]
                        ) -> Tuple[float, float, float, float]:
    x1, y1, x2, y2 = s1
    x3, y3, x4, y4 = s2

    dx1:float = x2 - x1
    dy1:float = y2 - y1
    dx2:float = x4 - x3
    dy2:float = y4 - y3

    denom:float = dx1 * dy2 - dy1 * dx2

    # 평행/공선
    if abs(denom) < EPS_DENOM:
        cand1 = ((x1, y1, 0.0), (x2, y2, 1.0))
        cand2 = ((x3, y3, 0.0), (x4, y4, 1.0))
        for px, py, t1 in cand1:
            for qx, qy, t2 in cand2:
                if px == qx and py == qy:
                    return px, py, t1, t2
        return x1, y1, 0.0, 0.0

    qpx:float = x3 - x1
    qpy:float = y3 - y1

    t1:float = (qpx * dy2 - qpy * dx2) / denom
    t2:float = (qpx * dy1 - qpy * dx1) / denom

    tiny:float = 1e-12
    if t1 < 0.0 and t1 > -tiny:
        t1 = 0.0
    if t1 > 1.0 and t1 < 1.0 + tiny:
        t1 = 1.0
    if t2 < 0.0 and t2 > -tiny:
        t2 = 0.0
    if t2 > 1.0 and t2 < 1.0 + tiny:
        t2 = 1.0

    x:float = x1 + t1 * dx1
    y:float = y1 + t1 * dy1
    return x, y, t1, t2

def evalue_D(du: float, dv: float, L: float, s: float) -> float:
    best:float = INF
    if du < INF:
        TEMP:float = du + s
        if TEMP < best:
            best = TEMP
    if dv < INF:
        TEMP = dv + (L - s)
        if TEMP < best:
            best = TEMP
    return best

def best_on_edge_intervalue(du: float, dv: float, L: float,
                            pL: float, pR: float) -> float:
    if du >= INF and dv >= INF:
        return INF
    best:float = INF

    v:float = evalue_D(du, dv, L, pL)
    if v < best:
        best = v
    if pR != pL:
        v = evalue_D(du, dv, L, pR)
        if v < best:
            best = v

    if du < INF and dv < INF:
        s_star:float = (dv - du + L) * 0.5
        if s_star >= pL - 1e-12 and s_star <= pR + 1e-12:
            v = evalue_D(du, dv, L, s_star)
            if v < best:
                best = v
    return best

# ===== 세그먼트 트리 (함수 버전) =====

def build_segtree(values: List[float]) -> Tuple[int, List[float]]:
    m:int = len(values)
    if m == 0:
        return 0, []
    n:int = 1
    while n < m:
        n <<= 1
    seg:List[float] = [INF] * (2 * n)
    for i, v in enumerate(values):
        seg[n + i] = v
    for i in range(n - 1, 0, -1):
        left: float = seg[i << 1]
        right: float = seg[i << 1 | 1]
        seg[i] = left if left < right else right
    return n, seg

def seg_range_min(seg: List[float], n: int, l: int, r: int) -> float:
    if n == 0 or l >= r:
        return INF
    res:float = INF
    l += n
    r += n
    while l < r:
        if l & 1:
            if seg[l] < res:
                res = seg[l]
            l += 1
        if r & 1:
            r -= 1
            if seg[r] < res:
                res = seg[r]
        l >>= 1
        r >>= 1
    return res

# SegmentData 대체 : dict로 관리
def make_segment_data() -> Dict[str, Any]:
    return {
        'sx': 0.0, 'sy': 0.0, 'ex': 0.0, 'ey': 0.0,
        'len': 0.0,
        'nodes': [],      # type: List[int]
        'spos': [],       # type: List[float]
        'edgeLen': [],    # type: List[float]
        'edgeMin': [],    # type: List[float]
        'st_n': 0,        # type: int
        'st_seg': [],     # type: List[float]
        'usable': False,  # type: bool
    }

out_lines:List[str] = []

T:int = int(input().rstrip())

for _ in range(T) :
    # n, R
    n_R = input().split()
    while len(n_R) < 2 :
        n_R += input().split()
    n:int = int(n_R[0])
    R:float = float(n_R[1])
    R2:float = R * R

    segments:List[Tuple[float, float, float, float]] = [None] * n  # type : ignore
    seg_pts:List[List[Tuple[float, int]]] = [[] for _ in range(n)]  # (t, node_id)

    total_fs:int = 0

    # 점 목록 + 좌표 -> id 매핑
    points:List[Tuple[float, float]] = []
    points_append = points.append
    point_id:Dict[Tuple[int, int], int] = {}

    def get_pid(x: float, y: float,
                _pid: Dict[Tuple[int, int], int] = point_id,
                _append=points_append) -> int:
        rx:int = int(round(x * KEY_PREC_SCALE))
        ry:int = int(round(y * KEY_PREC_SCALE))
        key = (rx, ry)
        pid = _pid.get(key)
        if pid is not None:
            return pid
        pid = len(points)
        _append((rx / KEY_PREC_SCALE, ry / KEY_PREC_SCALE))
        _pid[key] = pid
        return pid

    fire_nodes:Set[int] = set()

    # 도로 입력 + 소방서 위치 처리
    for i in range(n):
        parts: List[str] = input().split()
        while len(parts) < 5:
            parts += input().split()

        sx:float = float(parts[0])
        sy:float = float(parts[1])
        ex:float = float(parts[2])
        ey:float = float(parts[3])
        m:int = int(parts[4])

        segments[i] = (sx, sy, ex, ey)
        total_fs += m

        id_s:int = get_pid(sx, sy)
        id_e:int = get_pid(ex, ey)
        seg_pts[i].append((0.0, id_s))
        seg_pts[i].append((1.0, id_e))

        coeffs:List[float] = []
        index:int = 5
        # 나머지 m개 c 읽기 (여러 줄에 걸쳐 있을 수 있음)
        while len(coeffs) < m:
            while index < len(parts) and len(coeffs) < m:
                coeffs.append(float(parts[index]))
                index += 1
            if len(coeffs) < m:
                parts = input().split()
                index = 0

        for c in coeffs:
            x:float = sx + (ex - sx) * c
            y:float = sy + (ey - sy) * c
            pid:int = get_pid(x, y)
            seg_pts[i].append((c, pid))
            fire_nodes.add(pid)

    # Q, 그리고 Q개의 쿼리
    query:list = input().split()
    while len(query) == 0:
        query = input().split()
    Q:int = int(query[0])

    queries:List[Tuple[float, float]] = []
    for _ in range(Q):
        parts = input().split()
        while len(parts) < 2:
            parts += input().split()
        qx: float = float(parts[0])
        qy: float = float(parts[1])
        queries.append((qx, qy))

    # 소방서가 하나도 없으면 모든 화재는 -1
    if total_fs == 0:
        out_lines.extend(["-1"] * Q)
        continue

    # --- 도로들 사이의 교점(선분-선분 교차) ---
    for i in range(n):
        s1 = segments[i]
        for j in range(i + 1, n):
            s2 = segments[j]
            if not segments_intersect(s1, s2):
                continue
            x, y, t1, t2 = intersection_params(s1, s2)
            pid = get_pid(x, y)
            seg_pts[i].append((t1, pid))
            seg_pts[j].append((t2, pid))

    # --- 정점 수 확정, 인접 리스트, 선분 데이터 준비 ---
    Nnodes:int = len(points)
    adj:List[List[Tuple[int, float]]] = [[] for _ in range(Nnodes)]
    segData:List[Dict[str, Any]] = [make_segment_data() for _ in range(n)]

    for i in range(n):
        sp:List[Tuple[float, int]] = seg_pts[i]
        sp.sort(key=lambda p: p[0])

        # 연속 중복 노드 제거
        unique:List[Tuple[float, int]] = []
        last_node:int = -1
        for t, nid in sp:
            if nid != last_node:
                unique.append((t, nid))
                last_node = nid
        sp = unique

        K:int = len(sp)
        if K < 2:
            continue

        seg = make_segment_data()
        sx, sy, ex, ey = segments[i]
        seg['sx'] = sx
        seg['sy'] = sy
        seg['ex'] = ex
        seg['ey'] = ey
        dx:float = ex - sx
        dy:float = ey - sy
        seg['len'] = math.hypot(dx, dy)

        nodes:List[int] = [0] * K
        spos:List[float] = [0.0] * K
        edgeLen:List[float] = [0.0] * (K - 1)

        first_node:int = sp[0][1]
        nodes[0] = first_node
        spos[0] = 0.0
        px, py = points[first_node]

        for k in range(1, K):
            node:int = sp[k][1]
            nodes[k] = node
            qx, qy = points[node]
            ddx:float = qx - px
            ddy:float = qy - py
            L:float = math.hypot(ddx, ddy)
            edgeLen[k - 1] = L
            spos[k] = spos[k - 1] + L

            u:int = sp[k - 1][1]
            v:int = node
            if u != v and L >= 0.0:
                adj[u].append((v, L))
                adj[v].append((u, L))

            px, py = qx, qy

        seg['nodes'] = nodes
        seg['spos'] = spos
        seg['edgeLen'] = edgeLen
        seg['edgeMin'] = []
        seg['usable'] = False
        seg['st_n'] = 0
        seg['st_seg'] = []

        segData[i] = seg

    # --- 멀티 소스 다익스트라 ---
    distance:List[float] = [INF] * Nnodes
    pq:List[Tuple[float, int]] = []

    for src in fire_nodes:
        distance[src] = 0.0
        pq.append((0.0, src))
    heapq.heapify(pq)

    while pq:
        d, u = heapq.heappop(pq)
        if d != distance[u]:
            continue
        for v, w in adj[u]:
            nd:float = d + w
            if nd < distance[v]:
                distance[v] = nd
                heapq.heappush(pq, (nd, v))

    # --- 각 도로마다 edgeMin 계산 + 세그먼트 트리 구축 ---
    for i in range(n):
        seg = segData[i]
        nodes = seg['nodes']
        K = len(nodes)
        if K < 2:
            seg['usable'] = False
            seg['st_n'], seg['st_seg'] = 0, []
            continue

        edgeLen = seg['edgeLen']
        M:int = K - 1
        edgeMin:List[float] = [INF] * M
        anyFinite:bool = False

        for j in range(M):
            u = nodes[j]
            v = nodes[j + 1]
            du:float = distance[u]
            dv:float = distance[v]
            L = edgeLen[j]

            if du >= INF and dv >= INF:
                edgeMin[j] = INF
                continue

            best:float = INF
            if du < INF and du < best:
                best = du
            if dv < INF and dv < best:
                best = dv

            if du < INF and dv < INF:
                s_star:float = (dv - du + L) * 0.5
                if 0.0 < s_star < L:
                    value = evalue_D(du, dv, L, s_star)
                    if value < best:
                        best = value

            edgeMin[j] = best
            if best < INF:
                anyFinite = True

        seg['edgeMin'] = edgeMin
        seg['usable'] = anyFinite
        if anyFinite:
            seg['st_n'], seg['st_seg'] = build_segtree(edgeMin)
        else:
            seg['st_n'], seg['st_seg'] = 0, []

    # --- 쿼리 처리 ---
    for (qx, qy) in queries:
        result:float = INF

        for i in range(n):
            seg = segData[i]
            if not seg['usable']:
                continue

            sx = seg['sx']; sy = seg['sy']
            ex = seg['ex']; ey = seg['ey']
            dx = ex - sx
            dy = ey - sy
            Ltot2:float = dx * dx + dy * dy
            if Ltot2 <= 0.0:
                continue

            # 선분-원 교차
            fx:float = sx - qx
            fy:float = sy - qy
            a:float = Ltot2
            b:float = 2.0 * (dx * fx + dy * fy)
            c:float = fx * fx + fy * fy - R2

            disc:float = b * b - 4.0 * a * c
            if disc < -EPS_DISC:
                continue
            if disc < 0.0:
                disc = 0.0

            sqrt_disc:float = math.sqrt(disc)
            t1:float = (-b - sqrt_disc) / (2.0 * a)
            t2:float = (-b + sqrt_disc) / (2.0 * a)
            if t1 > t2:
                t1, t2 = t2, t1

            if t1 > 1.0 or t2 < 0.0:
                continue
            t_low:float = t1 if t1 > 0.0 else 0.0
            t_high:float = t2 if t2 < 1.0 else 1.0
            if t_low > t_high:
                continue

            Ltot:float = seg['len']
            if Ltot <= 0.0:
                continue
            sL:float = Ltot * t_low
            sR:float = Ltot * t_high
            if sL > sR:
                sL, sR = sR, sL

            spos = seg['spos']
            endS:float = spos[-1]
            if sL < 0.0:
                sL = 0.0
            if sR > endS:
                sR = endS
            if sR < sL:
                continue

            K = len(spos)
            if K < 2:
                continue
            M = K - 1

            jL:int = bisect_right(spos, sL) - 1
            jR:int = bisect_right(spos, sR) - 1
            if jL < 0:
                jL = 0
            if jL >= M:
                jL = M - 1
            if jR < 0:
                jR = 0
            if jR >= M:
                jR = M - 1

            nodes = seg['nodes']
            edgeLen = seg['edgeLen']
            st_n:int = seg['st_n']
            st_seg = seg['st_seg']

            best:float = INF

            if jL == jR:
                edgeStart:float = spos[jL]
                pL:float = sL - edgeStart
                pR:float = sR - edgeStart
                if pL < 0.0:
                    pL = 0.0
                L:float = edgeLen[jL]
                if pR > L:
                    pR = L
                u = nodes[jL]
                v = nodes[jL + 1]
                du = distance[u]
                dv = distance[v]
                if du < INF or dv < INF:
                    value = best_on_edge_intervalue(du, dv, L, pL, pR)
                    if value < best:
                        best = value
            else:
                # 왼쪽 부분 간선
                j = jL
                edgeStart = spos[j]
                edgeEnd = spos[j + 1]
                pL = sL - edgeStart
                if pL < 0.0:
                    pL = 0.0
                L = edgeLen[j]
                pR = edgeEnd - edgeStart
                if pR > L:
                    pR = L
                u = nodes[j]
                v = nodes[j + 1]
                du = distance[u]
                dv = distance[v]
                if du < INF or dv < INF:
                    value = best_on_edge_intervalue(du, dv, L, pL, pR)
                    if value < best:
                        best = value

                # 오른쪽 부분 간선
                j = jR
                edgeStart = spos[j]
                L = edgeLen[j]
                pL = 0.0
                pR = sR - edgeStart
                if pR > L:
                    pR = L
                if pR < 0.0:
                    pR = 0.0
                u = nodes[j]
                v = nodes[j + 1]
                du = distance[u]
                dv = distance[v]
                if du < INF or dv < INF:
                    value = best_on_edge_intervalue(du, dv, L, pL, pR)
                    if value < best:
                        best = value

                # 가운데 완전히 포함된 간선들
                if jL + 1 <= jR - 1 and st_n > 0:
                    l = jL + 1
                    r = jR  # [l, r)
                    value = seg_range_min(st_seg, st_n, l, r)
                    if value < best:
                        best = value

            if best < result:
                result = best

        if result >= INF:
            out_lines.append("-1")
        else:
            out_lines.append(f"{result:.20f}")

print("\n".join(out_lines))