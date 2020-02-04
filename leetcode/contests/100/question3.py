class Solution {
    public int subarrayBitwiseORs(int[] A) {
        HashSet<Integer> result= new HashSet<Integer>();
        HashSet<Integer> prev= new HashSet<Integer>();
        for (Integer i : A){
            HashSet<Integer> temp= new HashSet<Integer>();
            temp.add(i);
            for(Integer j :prev){
                temp.add(i|j);
            }
            prev=temp;
            result.addAll(prev);
        }
        return result.size();
    }
}