int findMin(int* nums, int numsSize) {

    int l =0,r=numsSize-1,mid;
    int result=0;
    while (l<r){
        mid=l+(r-l)/2;
        if (nums[mid]>nums[r]){

            l=mid+1;

        }
        else{
            r=mid;

        }
    }
    return nums[l];

    
}