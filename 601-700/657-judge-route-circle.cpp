class Solution {
public:
    bool judgeCircle(string moves) {
        int flag_lr = 0;
		int flag_ud = 0;
		for (int i = 0; i < moves.length();i++){
			if(moves[i] == 'R')
				flag_lr++;
			else if(moves[i] == 'L')
				flag_lr--;
			else if(moves[i] == 'U')
				flag_ud++;
			else if(moves[i] == 'D')
				flag_ud--;
		}
		if(flag_lr == 0 && flag_ud == 0)
			return true;
		else return false;
    }
};