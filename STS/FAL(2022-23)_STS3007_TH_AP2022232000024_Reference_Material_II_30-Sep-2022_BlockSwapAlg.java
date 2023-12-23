class BlockSwapAlg{
    static int arr[]={1,2,3,4,5,6,7};

    public static void swap(int first, int sec, int r){
        for(int i = 0 ; i < r ; i++){
            int temp = arr[first + i]; 
            arr[first + i] = arr[sec + i]; 
            arr[sec + i] = temp;
        }
    }
    
    public static void main(String[] args){
        int n = arr.length, r = 4, i = r, j = n - r;
        
        if(r!=0 && r!=n){
           
            while (i != j){
                if(i < j){
                    swap(r-i, r+j-i, i);
                    j = j - i;
            }
                else{
                    swap(r-i, r, j);
                    i = i - j;
                }
            }
            swap( r-i, r, i);
        }
        
        System.out.println("Array Elements after rotating : "); 
        for(int k = 0 ; k < n ; k++)
            System.out.print(arr[k] + " ");
    }
}
