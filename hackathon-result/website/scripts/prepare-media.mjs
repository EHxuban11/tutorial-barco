import { readdir, mkdir, copyFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
const source = new URL("../../videos/", import.meta.url);
const destination = new URL("../public/video/", import.meta.url);
await mkdir(destination, {recursive:true});
let count=0;
for (const file of await readdir(source)) {
  if (!/\.(mp4|jpg|png)$/i.test(file)) continue;
  await copyFile(new URL(file,source),new URL(file,destination)); count++;
}
console.log(`Prepared ${count} local media files.`);
