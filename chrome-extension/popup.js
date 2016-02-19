chrome.windows.getCurrent(function(win){
  chrome.tabs.getSelected(function(tab){
    var img,_width=200,_height=200;

    //console.log(tab);
    var url = tab.url;
    jQuery('#lurl').text(url);
    jQuery('#qrcode').qrcode({width:_width,height:_height,text:url});

    if(tab.favIconUrl){
      img = new Image();
      img.src = tab.favIconUrl;
      img.onload=function(){
        var _w = img.width,_h = img.height
        ,_x = 0 ,_y = 0
        ;
        if(_w && _h){
          drawImg(img,(_width-_w)/2,(_height-_h)/2);
        }
      };
    }

    cutUrl(url,function(data){
        url = data;
        jQuery("#surl").text(url);
      });

    jQuery("#cutBtn").bind("click",function(){
      cutUrl(url,function(data){
        url = data;
        jQuery("#lurl").text(url);
      });
    });


    jQuery("#shareQzone").bind("click",function(){
      doShare();
    });

    jQuery("#copyBtn").bind("click",function(){
      copyTextToClipboard(jQuery("#surl").text());
    });

  });
});

// Copy provided text to the clipboard.
function copyTextToClipboard(text) {
    var copyFrom = $('<textarea/>');
    copyFrom.text(text);
    $('body').append(copyFrom);
    copyFrom.select();
    document.execCommand('copy');
    copyFrom.remove();
}

function cutUrl(url,cb){
  jQuery.ajax({
    url:'http://dzm.la/s/url/',
    data:{u:url},
    type:'post',
    dataType:'text',
    success:function(data){
      cb("http://dzm.la/"+data);
    },
    error:function(e){
      alert(e);
    }
  });
}

function doShare(){
  cutUrl(jQuery('#surl').text(),function(u){
     window.open('http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url='+encodeURIComponent(u));
  });
  return false;
}


//加入图片
function drawImg(img,x,y){
    var myCanvas = document.getElementsByTagName('canvas')
        ,_canvas = myCanvas[0]
        ,myctx = _canvas.getContext('2d')
    ;
    myctx.drawImage(img,x||0,y||0);

}
