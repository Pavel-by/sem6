from math import *


def input_step():
    raw = input().split()

    if len(raw) < 5:
        return None

    return [int(raw[0]), float(raw[1]), float(raw[2]), float(raw[3]), int(raw[4])]


def print_step(step):
    print("{:>3d} {:<5f} {:<5f} {:<8f} {:2d} {:<5f} {:<5f}".format(*step))


x1 = 1
x2 = 1

prevStep = input_step()
prevStep.append(0)
prevStep.append(0)

steps = []
steps.append(prevStep)
#print(';'.join([str(round(i, 6)) for i in prevStep]))
#print_step(prevStep)

step = input_step()

while step is not None:
    prevDelta = sqrt((x1 - prevStep[1])**2 + (x2 - prevStep[2])**2)
    delta = sqrt((x1 - step[1])**2 + (x2 - step[2])**2)
    step.append(log(delta) / log(prevDelta))
    step.append(step[3] / prevStep[3])
    #print_step(step)
    #print(';'.join([str(round(i, 6)) for i in step]))
    steps.append(step)
    prevStep = step
    step = input_step()

for i in range(0, len(steps)):
    print(';'.join([str(round(i, 7)) for i in steps[i]]))