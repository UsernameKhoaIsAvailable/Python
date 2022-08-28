M = input("Nhap vao 1 so: ")
N = input("Nhap vao 1 so nua: ")
M = int(M)
N = int(N)
uocM = 0
uocN = 0

for i in range(1,M):
    if M % i == 0:
        uocM = uocM + i
for i in range(1,N):
    if N % i == 0:
        uocN =uocN + i

if uocM == N and uocN == M:
    print(M, "va ", N, "la 1 cap so than thiet")
else:
    print(M, "va ", N, "khong la 1 cap so than thiet")
