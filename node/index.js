var chokidar = require('chokidar');
var watcher = chokidar.watch('../firstCourse', {
    ignored: /[\/\\]\./, persistent: true
  });

  var exec = require('child_process').exec;
  function execute(cmd){
      console.log(cmd)
      exec(cmd, function(error, stdout, stderr) {
          if(error){
              console.error(error);
          }
          else{
            //   console.log("success");
          }
      });
      
    }
    watcher.on("change",(path)=>{
        execute("python "+path)
  })