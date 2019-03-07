#include<stdio.h>
#include<stdlib.h>

int swap(int *a, int indexToSwap) {
    int found = 0;
    int i = indexToSwap - 1;
    int value = a[i];
    int s = 0;
    while(!found && i>=0) {
        if(a[i] < value) { //scalino
            value = a[i];
            int temp = a[indexToSwap];
            a[indexToSwap] = a[i+1];
            a[i+1] = temp;
            s++;
            indexToSwap = i+1;
            if(indexToSwap > 0 && a[indexToSwap] < a[indexToSwap-1])
                s += swap(a, indexToSwap);
            else
                found = 1;
        } else i--;
    }
    if(i<0) {
        int temp = a[indexToSwap];
        a[indexToSwap] = a[0];
        a[0] = temp;
        s++;
    }
    return s;
}

int main(int argc, char* argv[]) {
	
    int N, s = 0, c;
    scanf("%d", &N);
    scanf("%d", &c);
    int a[N];

    int i = 0;
    while(i<N) {
        int b;
        scanf("%d", &b);
        if(b < c) {
            a[i++] = b;
        }
    }

    i=1;
    while(i<N) {
        if(a[i] < a[i-1])
            s += swap(a, i);
        i++;    
    }
    printf("%d", s);
}