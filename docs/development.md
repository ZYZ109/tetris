# 开发文档

## 开发环境设置
1. 克隆项目
```bash
git clone <repository-url>
cd tetris
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

## 项目结构
- `src/`: 源代码目录
  - `game/`: 游戏核心逻辑
  - `states/`: 状态管理
  - `ui/`: 用户界面
  - `utils/`: 工具函数

## 开发规范
1. 代码风格遵循 PEP 8
2. 所有函数和类都需要添加文档字符串
3. 使用类型提示
4. 添加适当的日志记录

## 测试
1. 运行测试
```bash
pytest
```

2. 查看测试覆盖率报告
```bash
pytest --cov=src --cov-report=html
```

## 发布流程
1. 更新版本号
2. 更新 CHANGELOG.md
3. 创建发布标签
4. 构建和发布包 