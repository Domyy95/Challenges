#include<stdio.h>
#include<stdlib.h>

// is easy after you notice that each odd window can interacts only with the next one
int main(int argc, char* argv[]) {
	
	int N, H, W, sum, prev, next, area = 0;
	scanf("%d", &N);
	scanf("%d", &H);
	scanf("%d", &W);

	for(int i=0; i<N; i++) {
        if(i % 2 == 0) {
            scanf("%d", &prev);
        } else {
        	scanf("%d", &next);
        	sum = prev + next;
            if(sum <= W) {
                area += sum;
            } else {
                area += 2 * W - sum;
            }
        }
    }
    printf("%d", area * H);
}