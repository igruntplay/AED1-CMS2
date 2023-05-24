#!/bin/bash

echo -e "\nEmpates:"
python3 Ej1-PiedraPapelTijera.py << EOF
Piedra Piedra
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Tijera Tijera
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Papel Papel
EOF

echo -e "\nJugador1:"
python3 Ej1-PiedraPapelTijera.py << EOF
Piedra Tijera
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Tijera Papel
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Papel Piedra
EOF

echo -e "\nJugador2:"
python3 Ej1-PiedraPapelTijera.py << EOF
Tijera Piedra
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Papel Tijera
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Piedra Papel
EOF

echo -e "\nCadenas con Espacios:"
python3 Ej1-PiedraPapelTijera.py << EOF
 Piedra Tijera
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Tijera  Papel
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
 Papel Piedra 
EOF

echo -e "\nCaso Sensitivo:"
python3 Ej1-PiedraPapelTijera.py << EOF
piedra Tijera
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Tijera papel
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
papel Piedra
EOF

echo -e "\nCaracteres Especiales o Números:"
python3 Ej1-PiedraPapelTijera.py << EOF
Piedra123 Tijera
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Tijera! Papel
EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Papel! Piedra123
EOF

echo -e "\nCadenas Vacías:"
python3 Ej1-PiedraPapelTijera.py << EOF

EOF
python3 Ej1-PiedraPapelTijera.py << EOF
Piedra 
EOF
