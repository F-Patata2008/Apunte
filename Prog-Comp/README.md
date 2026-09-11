# Programación Competitiva — Uchile / ICPC

Material y cheat-sheets de algoritmos y estructuras de datos para **Programación Competitiva** (Comunidad de ProgComp FCFM Universidad de Chile, ICPC, OCI, IOI).

---

## 📂 Contenido

```
Prog-Comp/
├── Apunte_Selectivo.tex   # Código fuente en LaTeX con snippets de C++
├── Apunte_Selectivo.pdf   # Documento compilado listo para consulta rápida
└── images -> ../images    # Enlace relativo a recursos gráficos
```

---

## 📑 Temario del Apunte

El apunte [`Apunte_Selectivo.pdf`](./Apunte_Selectivo.pdf) incluye implementaciones optimizadas en **C++20**:

1. **Plantillas Base:**
   - Fast I/O (`ios_base::sync_with_stdio(0); cin.tie(0)`), macros y plantillas multi-test case.
2. **Estructuras de Datos:**
   - Segment Tree (Point Update, Range Minimum / Maximum Query).
   - Fenwick Tree / Binary Indexed Tree (BIT).
   - Disjoint Set Union (DSU / Union-Find con compresión de caminos y unión por rango).
3. **Algoritmos de Grafos:**
   - Recorridos: Búsqueda en Profundidad (DFS) y Búsqueda en Anchura (BFS).
   - Caminos Mínimos: Dijkstra con `priority_queue` optimizada.
   - Árbol Recubridor Mínimo (MST): Algoritmo de Kruskal.
   - Detección de ciclos y componentes conexas.
4. **Programación Dinámica (DP):**
   - Problemas clásicos (mochila / knapsack, subsecuencia común más larga, etc.).
5. **Trucos y buenas prácticas de STL en C++:**
   - Complejidades temporales y consideraciones de memoria para jueces en línea (Codeforces, AtCoder, CSES).

---

## 🛠️ Compilación
```bash
cd Prog-Comp
pdflatex Apunte_Selectivo.tex
```
