package BOJ.dataStructure;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class NHNPreTest {
    static int N;
    static int[][] map;
    static int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    static List<Integer> groupList;

    public static void main(String[] args) throws IOException {
        // 입력받을 객체 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st; // 파이썬 split같은거, String을 구분자 기준으로 parse해서 가지고 있음
        map = new int[N][N];
        groupList = new LinkedList<>();
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for(int j = 0; j < N; j++) {
                // nestToken() st가 가지고 잇는 parse된 데이터를 앞에서 부터 하나씩 string꺼내주는애
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int r = 0; r < N; r++) {
            for(int c = 0; c < N; c++) {
                if(map[r][c] == 0) continue;

                int size = bfs(r, c);
                groupList.add(size);
            }
        }

        System.out.println(groupList.size());
        Collections.sort(groupList);
        for(int group: groupList) {
            System.out.print(group + " ");
        }
        System.out.println();
    }

    public static int bfs(int r, int c) {
        int cnt = 0;

        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(r, c));
        map[r][c] = 0;

        while(!q.isEmpty()) {
            Pos cur = q.poll();
            cnt++;

            for(int d = 0; d < 4; d++) {
                int nr = cur.r + dir[d][0];
                int nc = cur.c + dir[d][1];

                if(nr < 0 || nc < 0 || nr >= N || nc >= N || map[nr][nc] == 0) continue;

                map[nr][nc] = 0;
                q.add(new Pos(nr, nc));
            }
        }

        return cnt;
    }

    public static class Pos{
        int r, c;
        Pos(int r, int c){
            this.r = r;
            this.c = c;
        }
    }
}