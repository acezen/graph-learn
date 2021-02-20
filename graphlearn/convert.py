
import numpy as np

def process():
    nodes = np.genfromtxt("paper_with_label.csv", dtype=np.dtype(str))
    edges = np.genfromtxt("paper_cites_paper.csv", dtype=np.dtype(str))
    with open("gl_paper.csv", "w") as f:
        header = "id:int64\tlabel:int64\tfeature:string"
        f.write(header + "\n")
        for i in range(len(nodes)):
            if i == 0:
                continue
            line = nodes[i][0] + "\t" + nodes[i][130] + "\t" + nodes[i][1:129]
            f.write(line + "\n")
    with open("gl_paper_edge.csv", "w") as f:
        header = "src_id:int64" + "\t" "dst_id:int64"
        f.write(header + "\n")
        for i in range(len(edges)):
            if i == 0:
                continue
            line = edges[i][0] + "\t" + edges[i][1]
            f.write(line + "\n")

if __name__ == "__main__":
    process()
