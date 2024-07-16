import matplotlib.pyplot as plt
import numpy as np

def read_joint_positions(filename):
    # 读取文件内容
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    # 解析文件内容
    joint_positions = []
    for line in lines:
        positions = list(map(float, line.strip().split()))
        joint_positions.append(positions)
    
    return np.array(joint_positions)

def compute_velocities(joint_positions, dt=1.0):
    # 计算关节速度
    velocities = np.diff(joint_positions, axis=0) / dt
    return velocities

def compute_accelerations(velocities, dt=1.0):
    # 计算关节加速度
    accelerations = np.diff(velocities, axis=0) / dt
    return accelerations

def plot_joint_data(joint_data, ylabel, title, output_file):
    # 创建一个新的图形
    plt.figure(figsize=(10, 6))
    
    # 绘制每个关节的数据曲线
    for i in range(joint_data.shape[1]):
        plt.plot(joint_data[:, i], label=f'Joint {i+1}')
    
    # 添加图例
    plt.legend()
    
    # 添加标题和标签
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel(ylabel)
    
    # 保存图形为文件
    plt.savefig(output_file)
    plt.close()

if __name__ == "__main__":
    # 替换为你的实际文件路径
    input_file = '0716_traj_cubitspline.txt'
    position_file = 'joint_positions.png'
    velocity_file = 'joint_velocities.png'
    acceleration_file = 'joint_accelerations.png'

    # 读取关节位置数据
    joint_positions = read_joint_positions(input_file)

    # 计算关节速度和加速度
    joint_velocities = compute_velocities(joint_positions)
    joint_accelerations = compute_accelerations(joint_velocities)

    # 绘制并保存图形
    plot_joint_data(joint_positions, 'Position', 'Joint Positions Over Time', position_file)
    plot_joint_data(joint_velocities, 'Velocity', 'Joint Velocities Over Time', velocity_file)
    plot_joint_data(joint_accelerations, 'Acceleration', 'Joint Accelerations Over Time', acceleration_file)

    print(f'Joint positions plot saved as {position_file}')
    print(f'Joint velocities plot saved as {velocity_file}')
    print(f'Joint accelerations plot saved as {acceleration_file}')
