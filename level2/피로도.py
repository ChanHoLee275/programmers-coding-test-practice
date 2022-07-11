function sub_list(list1, list2){
    const set1 = new Set(list1);
    list2.forEach(el => {
        set1.delete(el);
    });
    return [... set1];
}


function solution(k, dungeons) {
    var answer = -1;
    // [indexs, remain]
    const queue = [];
    const indexs = new Array(dungeons.length).fill(0).map((_, idx) => idx);
    dungeons.forEach((el, idx) => {
       if(el[0] <= k){
           queue.push([idx, k - el[1]])
       }
    });
    while(queue.length !== 0){
        const target = queue.pop();
        const remain = target.pop();
        const candidate_indexs = sub_list(indexs, target);
        if(candidate_indexs.length == 0){
            return dungeons.length;
        }
        candidate_indexs.forEach(el => {
           if(dungeons[el][0] <= remain){
               queue.push([el, ...target, remain - dungeons[el][1]])
           }
            else{
               if(answer < target.length){
                   answer = target.length;
               }
           }
        });
    }
    return answer;
}
