"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const ytdl_core_1 = __importDefault(require("ytdl-core"));
const prompts_1 = __importDefault(require("prompts"));
(0, prompts_1.default)({
    type: 'text',
    name: "uri",
    message: "URI de la vidéo"
}).then(res => {
    console.log(res);
    ytdl_core_1.default.getInfo('https://www.youtube.com/watch?v=mImFz8mkaHo').then(a => {
        console.log(a);
    });
});
