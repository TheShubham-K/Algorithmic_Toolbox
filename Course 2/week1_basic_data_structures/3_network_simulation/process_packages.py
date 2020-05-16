# python3

from collections import namedtuple
from collections import deque
# Request = namedtuple("Request", ["arrived_at", "time_to_process"])
# Response = namedtuple("Response", ["was_dropped", "started_at"])

# class Buffer:
#     def __init__(self, size):
#         self.size = size
#         self.finish_time = []

#     def process(self, request):
#         arrived_at, time_to_process = request
#         while len(self.finish_time) > 0:
#             if self.finish_time[0] <= arrived_at:
#                 self.finish_time.pop(0)
#             else:
#                 break
#         if len(self.finish_time) == self.size:
#             return Response(True, -1)

#         if len(self.finish_time) == 0:
#             self.finish_time = [arrived_at + time_to_process]
#             return Response(False, arrived_at)

#         last_request = self.finish_time[-1]
#         self.finish_time.append(last_request + time_to_process)
#         return Response(False, last_request)

# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.process(request))
#     return responses


# def main():
#     buffer_size, n_requests = map(int, input().split())
#     requests = []
#     for _ in range(n_requests):
#         arrived_at, time_to_process = map(int, input().split())
#         requests.append(Request(arrived_at, time_to_process))

#     buffer = Buffer(buffer_size)
#     responses = process_requests(requests, buffer)

#     for response in responses:
#         print(response.started_at if not response.was_dropped else -1)


# if __name__ == "__main__":
#     main()


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = deque([])

    def Process(self, request):
        # write your code here
        if not self.finish_time_:
            self.finish_time_.append(
                request.process_time + request.arrival_time)
            return (Response(False, request.arrival_time))
        if request.arrival_time >= self.finish_time_[0]:
            i = 0
            while self.finish_time_[i] <= request.arrival_time:
                self.finish_time_.popleft()
                i += 1
                if i > len(self.finish_time_)-1:
                    break
            if self.finish_time_:
                added_time = self.finish_time_[-1]
            if not self.finish_time_:
                added_time = 0
            if request.arrival_time >= added_time:
                self.finish_time_.append(
                    request.process_time + request.arrival_time)
                return (Response(False, request.arrival_time))
            else:
                self.finish_time_.append(request.process_time + added_time)
                return (Response(False, added_time))
        if len(self.finish_time_) == self.size:
            return (Response(True, -1))
        if len(self.finish_time_) < self.size:
            added_time = self.finish_time_[-1]
            self.finish_time_.append(request.process_time + added_time)
            return (Response(False, added_time))


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests


def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses


def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)
    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)
    PrintResponses(responses)


# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.Process(request))
#     return responses


# def main():
#     buffer_size, n_requests = map(int, input().split())
#     requests = []
#     for _ in range(n_requests):
#         arrived_at, time_to_process = map(int, input().split())
#         requests.append(Request(arrived_at, time_to_process))

#     buffer = Buffer(buffer_size)
#     responses = process_requests(requests, buffer)

#     for response in responses:
#         print(response.started_at if not response.was_dropped else -1)


# if __name__ == "__main__":
#     main()
