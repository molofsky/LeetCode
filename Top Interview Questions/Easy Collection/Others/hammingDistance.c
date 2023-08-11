/* 
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
*/  

int hammingDistance(int x, int y){
    int count = 0, xor = x ^ y;
    
    for (int i = 0; i < 31; i++) {
        if (xor & 1) count++;
        xor >>= 1;
    }
    return count;
}
