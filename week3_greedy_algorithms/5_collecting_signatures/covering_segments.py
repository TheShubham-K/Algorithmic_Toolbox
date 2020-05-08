# Uses python3
import sys
import pdb
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    sortedsegs = sorted(segments, key = lambda t: t[1])
    #print(sortedsegs)
    #pdb.set_trace()
    point = sortedsegs[0].end
    points.append(point)
    for s in sortedsegs:
        if s.start > point:
            points.append(s.end)
            point = s.end
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    #print(*points)
    for p in points:
        print(p, end=' ')