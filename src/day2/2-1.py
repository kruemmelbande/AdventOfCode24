def issafe(report):
    if report == sorted(report) or list(reversed(report)) == sorted(report):
        report.sort()
        for i in range(1,(len(report))):
            if not (0<report[i] - report[i-1]<4):
                return False
        return True
    return False

with open('inputs/2', 'r') as f:
    reports = f.readlines()

a = 0
for count, i in enumerate(reports):
    report = [int(k) for k in i.split()]
    print(count, issafe(report))
    a += issafe(report)
print(a)