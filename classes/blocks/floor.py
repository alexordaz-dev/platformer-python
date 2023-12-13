class Floor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = self.get_floor_sprite(1)  # Inicializa el sprite con el nivel 1
        self.width = 7
        self.height = 7
    def update_status(self, current_level):
        # Cada 3 niveles, cambia el sprite del suelo
        if current_level % 3 == 0:
            self.sprite = self.get_floor_sprite(current_level)

    def get_floor_sprite(self, level):
        # Devuelve el sprite de suelo basado en el nivel
        if level % 3 == 0:
            # Cambia el sprite cada 3 niveles
            return (0,7,232,8,8)
        else:
            # Usa el sprite predeterminado para otros niveles
            return (0,0,224,8, 8)