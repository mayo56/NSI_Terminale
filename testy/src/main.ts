import ytdl from "ytdl-core";
import fs from "fs";

import prompt from "prompts";

prompt({
    type: 'text',
    name: "uri",
    message: "URI de la vidéo"
}).then(res => {
    console.log(res)
    ytdl.getInfo('https://www.youtube.com/watch?v=mImFz8mkaHo').then(a => {
        console.log(a)
    })
})