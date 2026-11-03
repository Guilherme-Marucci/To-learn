import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const source = readFileSync('C:/Users/PC/OneDrive - Educacional/Documentos/GitHub/Painel_Requisicao-REQ_NEW/Painel_Requisicao-REQ_NEW/REQUISICAO/prototipo-requisicoes/app.js', 'utf8');
const lesson = readFileSync(new URL('./Aprenda-construindo.md', import.meta.url), 'utf8').replaceAll('\r\n', '\n');

function setup(code) {
  const nodes = new Map();
  const node = id => {
    if (!nodes.has(id)) nodes.set(id, {
      value: '', textContent: '', innerHTML: '', hidden: false, dataset: {},
      classList: {toggle(){}, remove(){}, add(){}},
      insertAdjacentHTML(){}, addEventListener(){}, setAttribute(){}, focus(){}
    });
    return nodes.get(id);
  };
  const context = vm.createContext({
    document: {
      querySelector: node, querySelectorAll: () => [],
      documentElement: {dataset: {}}, addEventListener(){}
    },
    localStorage: {getItem: () => null, setItem(){}},
    HTMLDetailsElement: class {}, console
  });
  vm.runInContext(code, context);
  return {nodes, run: code => vm.runInContext(code, context)};
}

const original = setup(source);
const metricIds = ['#metric-total', '#metric-sectors', '#metric-email', '#metric-status'];
const counts = () => metricIds.map(id => original.nodes.get(id).textContent);
assert.deepEqual(counts(), ['12','5','3','9']);
original.run('state.sector="maintenance";render();');
assert.deepEqual(counts(), ['3','1','1','3']);
original.run('resetFilters();state.status="pending";render();');
assert.deepEqual(counts(), ['2','2','2','1']);
original.run('resetFilters();state.email="with";render();');
assert.deepEqual(counts(), ['3','3','3','2']);
original.run('resetFilters();state.query="zzzzzzzzz";render();');
assert.deepEqual(counts(), ['0','0','0','0']);
assert.equal(original.nodes.get('#empty-state').hidden, false);
assert.equal(original.run('searchable("MANUTENÇÃO")'), 'manutencao');
assert.equal(original.run('escapeHtml("A & B < C")'), 'A &amp; B &lt; C');

function snippet(section, language) {
  const text = lesson.split(section)[1];
  assert.ok(text, section);
  return text.split('```' + language + '\n')[1].split('```')[0].trim();
}
const properties = snippet('### Passo 2 — Ler o dado', 'javascript');
const markup = snippet('### Passo 3 — Mostrar o dado', 'html');
const search = snippet('### Passo 4 — Permitir encontrar', 'javascript');
const exercise = source
  .replace('email: false', 'responsavel: "Ana", email: false')
  .replace('const { id, status, branch, title, description, reference, deadline, item, email } = request;', properties)
  .replace('</dl>', markup + '</dl>')
  .replace(/return searchable\(\[request\.id[^\n]+/, search);
const amended = setup(exercise);
assert.match(amended.nodes.get('#sector-list').innerHTML, /<dd>Ana<\/dd>/);
assert.match(amended.nodes.get('#sector-list').innerHTML, /<dd>Não informado<\/dd>/);
amended.run('state.query="Ana";render();');
assert.match(amended.nodes.get('#sector-list').innerHTML, /data-card-id="20101"/);
console.log('Conferidos: contadores e filtros da aula, normalização, escape e exercício completo de responsável.');
