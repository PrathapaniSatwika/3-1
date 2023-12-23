import java.util.*;

class MaxEquilibriumSum{
	public static void main(String[] args){
		int arr[] = {-1,2,0,5,-2,3};
		int sum=0,res=0,prefix = 0;;
		
		for(int i=0;i<arr.length;i++)
		 sum += arr[i];
		
		for (int i = 0; i < arr.length; i++){
			prefix += arr[i];
			
			if (prefix == sum)
				res = Math.max(res,prefix);
			sum -= arr[i];
		}
		System.out.print(res);
	}
}
