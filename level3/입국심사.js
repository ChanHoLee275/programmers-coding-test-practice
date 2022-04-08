function solution(n, times) {
    var answer = 0;
    let minimum = 1;
    let maximum = Math.max(...times)*n;
    while(minimum <= maximum){
        let mid = Math.floor((minimum + maximum)/2);
        let people = 0;
        for(let i = 0; i < times.length; i++){
            people += Math.floor(mid / times[i]);
            if(people >= n){
                break;
            }
        }
        if(people >= n){
            answer = mid;
            maximum = mid - 1;
        }
        else if(people < n){
            minimum = mid + 1;
        }
    }
    return answer;
}
