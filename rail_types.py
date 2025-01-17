from dataclasses import dataclass

@dataclass
class BoundingBox:
    x1: float
    y1: float
    x2: float
    y2: float

    def __repr__(self):
        x1,x2 = min(self.x1,self.x2), max(self.x1,self.x2)
        y1,y2 = min(self.y1,self.y2), max(self.y1,self.y2)
        return f'{x1},{y1},{x2},{y2}'

@dataclass
class Signal:
    start_node_id: int
    node_id: int
    pos_x: float
    pos_y: float
    general: dict