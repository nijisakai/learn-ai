
let faceConfig = {
    face_token : '',
}
let faceAttributes = {};
 
function detectImg() {
    var r = new FileReader();
    f = document.getElementById('testImg').files[0];
    r.readAsDataURL(f);
    r.onload = function(e) {
        document.getElementById('img').src = this.result;
    }
    let url = 'https://api-cn.faceplusplus.com/facepp/v3/detect';
    let files = $('#testImg').prop('files');
    let data = new FormData();
    data.append('api_key', "r96Z6egn-dhhfNcHfEFIIhBJFN8IXKTk");
    data.append('api_secret', "2v6iB2fQndWfk-8dNNsCnYRhL7zSsFNF");
    data.append('image_file', files[0]);
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success(data) {
            faceConfig.face_token = data.faces[0].face_token;
            analyzeImg(); //调用分析图片的函数
        }
    })
}
 
function analyzeImg() {
    let url = 'https://api-cn.faceplusplus.com/facepp/v3/face/analyze';
    $.ajax({
        url: url,
        type: 'POST',
        data: {
            api_key: "r96Z6egn-dhhfNcHfEFIIhBJFN8IXKTk",
            api_secret: "2v6iB2fQndWfk-8dNNsCnYRhL7zSsFNF",
            face_tokens: faceConfig.face_token,
            return_attributes: "gender,age,smiling,ethnicity,skinstatus,eyestatus"
        },
        success(data) {
            // console.log(data);
            let attributes = data.faces[0].attributes;
            faceAttributes = {
                age : attributes.age.value,
                gender: attributes.gender.value,
                ethnicity: attributes.ethnicity.value,
                glass: attributes.glass.value,
                skinstatus: attributes.skinstatus
            }
            console.log(faceAttributes);
            //用jQuery获取模板
            var tpl   =  $("#tpl").html();
            //预编译模板
            var template = Handlebars.compile(tpl);
            //匹配json内容
            var html = template(faceAttributes);
            //输入模板
            $('#result').html(html);
        }
    })
}