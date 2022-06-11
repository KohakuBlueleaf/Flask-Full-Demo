/* initialize for socket.io */
let socket;
let sid;

function sio_init(){
  socket =  io('/chat', {'timeout':5000, 'connect timeout': 5000});
  socket.on('connect', function() {
    socket.emit('connect_event', {data: 'connected!'});
  });
  
  socket.on('server_response', function(msg) {
    console.log(msg, sid);
    $('#log-mes').text("Server: "+msg.data);
  });
  
  socket.on('reload_require', function(msg) {
    location.reload();
  });
  
  socket.on('sid_set', function(msg) {
    sid = msg.sid
    $('#log .meta').text("SID: " + sid);
  });
  
  socket.on('new_message', function(msg) {
    var msg_time = new Date(msg.time*1000);
    mes_app.messages.push({
      author: msg.author,
      time: msg_time.format("MM/dd hh:mm:ss"),
      content: msg.content
    })
    
    $('#mes-container').animate({
      scrollTop: $('#mes')[0].scrollHeight
    }, 10);
  });
}


/* bind message send to submit button */
function send_message() {
  if($('#mes_input').val()){
    socket.emit('client_event', {data: $('#mes_input').val()});
    $('#mes_input').val('');
  }
}
$('#submit').click(send_message);
$('#mes_input').keypress((e)=>{
  if(e.key == "Enter" && !e.shiftKey){
    send_message();
    e.preventDefault()
  }
})


/* bind scroll event */
$('#mes-container').scroll((e)=>{
  if($('#mes-container').scrollTop()==0){
    get_new();
  }
})


/* initialize */
let now_first = '';
let mes_app;
let mes_prev_height = 0;
const mes_component = {
  data(){
    return {
      messages: []
    }
  },
  delimiters: ['{[', ']}']
}

function init(){
  mes_app = createApp(mes_component).mount('#mes-container');
  get_new(true);
}

function get_new(scroll_bot=false){
  $.ajax({
    type: 'POST',
    url: '/chat/api/record',
    dataType: 'json',
    data: {
      start_from: now_first
    },
    success: (msgs)=>{
      msgs.forEach((msg)=>{
        var msg_time = new Date(msg.time*1000);
        mes_app.messages.insert(0, {
          author: msg.author,
          time: msg_time.format("MM/dd hh:mm:ss"),
          content: msg.content
        })
        now_first = msg.id;
      })

      if(scroll_bot){
        setTimeout(()=>{
          $('#mes-container').animate({
            scrollTop: $('#mes')[0].scrollHeight
          }, 1);
        }, 1)
      }else{
        setTimeout(()=>{
          $('#mes-container').animate({
            scrollTop: $('#mes')[0].scrollHeight-mes_prev_height-20
          }, 1);
        }, 1)
      }
      mes_prev_height = $('#mes')[0].scrollHeight;
    }
  })
}