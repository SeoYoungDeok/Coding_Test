#include <stdio.h>

int main(void) {
	int n, k;
	int cnt = 0;
	scanf("%d %d", &n, &k);
	
	int coin_list[n];

	for(int i=0;  i<n; i++){
	    scanf("%d", &coin_list[i]);
	}

	for(int i=n-1; i>=0; i--){
	    cnt += (int)k / coin_list[i];
	    k %= coin_list[i];
	}
	
	printf("%d", cnt);
}