function throttle(fn,delay){
    let prev=Date.now();

    return function(){
        let context=this;
        let arg=arguments;
        let now=Date.now();
        if(now-prev>=delay){
            fn.apply(context,arg);
            prev=Date.now()
        }
    }
}
function fn(){
    console.log("节流")
}

// addEventListener("scroll",throttle(fn,1000))