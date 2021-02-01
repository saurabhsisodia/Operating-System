from sys import stdin,stdout
def main():
    n=int(stdin.readline())
    bt=list(map(int,stdin.readline().split( )))
    
    wt=[0]*n;tat=[0]*n
    
    'waiting time for each process'
    for i in range(1,n):
        wt[i]=wt[i-1]+bt[i-1]
    
    
    'turnaround time for each process'
    for i in range(n):
        tat[i]=wt[i]+bt[i]
    
    
    stdout.write("avg waiting time:- %f"%(sum(wt)/n))
    stdout.write("avg turnaround time:- %f"%(sum(tat)/n))

main()
