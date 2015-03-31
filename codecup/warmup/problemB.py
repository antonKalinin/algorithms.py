balance = 0  # gru money balance
incomes_num = 0  # number of times gru receive money
boxes_sell = 0  # number of selling boxes
boxes_bought = 0  # number of bought boxes
exclude_receive_times = []  # list of times to exclude
box_cost = {'on_send': 0, 'on_receive': 0}
prompt = "> "

schedule = []  # list of events: incomes and sells
send2receive = {}  # dictionary matches box send and receive time

costs = input(prompt).split()

box_cost["on_receive"] = -int(costs.pop())
box_cost["on_send"] = -int(costs.pop())

incomes_num = int(input(prompt))

for i in range(0, incomes_num):
    income = input(prompt).split()
    schedule.append((int(income[1]), int(income[0])))

boxes_sell = int(input(prompt))

for i in range(0, boxes_sell):
    box_time = input(prompt).split()
    box_send_time = (int(box_time[0]))
    box_receive_time = (int(box_time[1]))

    schedule.append((box_send_time, box_cost["on_send"]))
    schedule.append((box_receive_time, box_cost["on_receive"]))

    send2receive[box_send_time] = box_receive_time

schedule = sorted(schedule, key=lambda event: event[0])

for j in range(0, len(schedule)):
    event = schedule[j]

    if event[1] >= 0:
        balance += event[1]

    # so we can buy free box too
    if event[1] <= 0:
        # if cost of box less than current balance
        # and gru did not buy that box earlier
        # gru buy the box, and increase the balance
        if balance >= abs(event[1]) and event[0] not in exclude_receive_times:
            balance += event[1]
            boxes_bought += 1

            if event[0] in send2receive:
                exclude_receive_times.append(send2receive[event[0]])

print(boxes_bought)
