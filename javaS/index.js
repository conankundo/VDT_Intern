console.log("ST");
let entityInfo = '{"adapter_id": "e7c06ba7-6d56-48eb-a2e4-d099846d4a02",'+
'"createdBy": "d7a55498-4fba-4162-bff6-3806f936622f",'+
'"destination": "adapter-2",' +
'"grpc_address": "adapter-0.viot-adapter:8957",'+
'"handle_msg_svc": "NV_e_sensor_aqua_payload",'+
'"name": "Adapter_e_sensor_aqua_deviceID",'+
'"owner": "d7a55498-4fba-4162-bff6-3806f936622f",'+
'"project_id": "aa04fe8a-02fe-4929-bae7-9a7f4c7a9fca",'+
'"sub_topic_regex": "innoway/pub2here",'+
'"thing_id": "8ce226f7-e2f7-4c5f-97e0-ffa094676c17",'+
'"topic": "innoway/pub2here",'+
'"user_id": "d7a55498-4fba-4162-bff6-3806f936622f"}';

// // test0_________________________________
let data = JSON.parse(entityInfo);
let example = data.topic;
console.log(entityInfo);
console.log(example);
let ex_str = JSON.stringify(example);
console.log(ex_str);
// // test1_________________________________
let btInput = "OFF";    
const msg = {"status"  : btInput };
let messagedata = JSON.stringify(msg)
console.log(messagedata)
// // test2_________________________________
msglen = entityInfo.length
bitrange = 16
remain = msglen % bitrange
loop = (msglen - remain)/bitrange
console.log(loop)
console.log(entityInfo.slice(0,5))
a = "123"
if (Number(a) != false){
    console.log("YES")
    console.log(Number(a))
}else{
    console.log("NO")
}
// for (let i = 0; i< loop; i++){
//     let str = entityInfo.slice(i*bitrange,(i+1)*bitrange)
//     console.l    
// }

    


