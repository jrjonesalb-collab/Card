import {readFile,writeFile,mkdir,copyFile} from 'node:fs/promises';
import {escapeHtml} from './build.mjs';
const people=JSON.parse(await readFile('employees.json','utf8'));
const jordan=people.find(p=>p.slug==='jordan-jones');
let html=await readFile('dist/jordan-jones/index.html','utf8');
html=html.replace('../styles.css','../option-b.css');
const a=jordan.address;
if(a){const old=['street','city','region','postalCode','country'].map(k=>a[k]).filter(Boolean).join(', ');const city=[a.city,[a.region,a.postalCode].filter(Boolean).join(' ')].filter(Boolean).join(', ');html=html.replace(`<strong>${escapeHtml(old)}</strong>`,`<strong>${escapeHtml(a.street)}<br>${escapeHtml(city)}${a.country?'<br>'+escapeHtml(a.country):''}</strong>`);}
await mkdir('dist/option-b',{recursive:true});
await writeFile('dist/option-b/index.html',html);
await copyFile('option-b.css','dist/option-b.css');
console.log('Separate comparison: /Card/option-b/');
