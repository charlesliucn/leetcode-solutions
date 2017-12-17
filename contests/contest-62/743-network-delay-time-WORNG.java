class Solution {
    public int networkDelayTime(int[][] times, int N, int K) {
        int[][] Graph = new int[N][N];
        for(int i=0; i < Graph.length; i++)
            for(int j=0; j< Graph[i].length; j++)
                Graph[i][j] = 10000;
        for(int i=0; i < times.length; i++)
            Graph[times[i][0]-1][times[i][1]-1] = times[i][2];
        for(int i=0; i < Graph.length; i++)
            for(int j=0; j< Graph[i].length; j++)
                System.out.print(" " + Graph[i][j]);
            System.out.println();
        int res = dijkstra(K, Graph);
        return res;
    }

    public static int dijkstra(int K, int[][] Graph) {
        int NUM = Graph[0].length;
        System.out.println(NUM);
        int[] prenode = new int[NUM];
        int[] mindist = new int[NUM];
        boolean[] find = new boolean[NUM];
         
        int vnear = 0;
         
        for (int i = 0; i < mindist.length; i++) {
            prenode[i] = i;
            mindist[i] = Graph[K][i];
            find[i] = false;
        }
 
        find[K] = true;
 
        for (int v = 0; v < Graph.length; v++) {
 
            int min = 10000;
            for (int j = 0; j < Graph.length; j++) {
                if (!find[j] && mindist[j] < min) {
                    min = mindist[j];
                    vnear = j;
                }
            }
            find[vnear] = true;
 
            for (int k = 0; k < Graph.length; k++) {
                if (!find[k] && (min + Graph[vnear][k]) < mindist[k]) {
                    prenode[k] = vnear;
                    mindist[k] = min + Graph[vnear][k];
                }
            }
        }
        
        for (int i = 0; i < NUM; i++) {
            System.out.println(find[i]);
            if (find[i] == false){
                return -1;
            }
                
        }
        int dist = 0;
        for (int i = 0; i < NUM; i++){
            dist += mindist[i]; 
        }
        return dist;
    }
}

