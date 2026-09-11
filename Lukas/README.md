# Lukas — Proyecto de Ingeniería (USACH)

Documentación técnica y planos de fabricación correspondientes al trabajo final de ingeniería mecánica y dibujo técnico para la **Universidad de Santiago de Chile (USACH)** por Lukas Espinoza.

---

## 📂 Contenido del Directorio

```
Lukas/
└── Trabajo_Final/
    ├── Trabajo_Final_Lukas_Espinoza.tex  # Documento principal en LaTeX
    ├── Trabajo_Final_Lukas_Espinoza.pdf  # Informe técnico final compilado
    ├── bibliografia.bib                 # Referencias bibliográficas
    ├── images/                          # Fotografías, esquemas y logos institucionales
    └── planos/                          # Planos de ingeniería normalizados
        ├── plano_conjunto.pdf           # Plano de ensamblaje general
        ├── plano_despiece.pdf           # Despiece de componentes
        ├── planos_fabricacion.pdf       # Cotas y tolerancias de manufactura
        └── projecto final_merged.pdf    # Entrega consolidada con memoria y planos
```

---

## 🛠️ Compilación
```bash
cd Lukas/Trabajo_Final
pdflatex Trabajo_Final_Lukas_Espinoza.tex
biber Trabajo_Final_Lukas_Espinoza
pdflatex Trabajo_Final_Lukas_Espinoza.tex
```
