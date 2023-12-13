```python
chart.animate(
    data,
    Config(
        {
            "channels": {
                "y": {"set": ["Popularity", "Kinds"]},
                "x": {"set": ["Genres"]},
                "color": {"set": ["Kinds"]},
                "label": {"set": ["Popularity"]},
            },
        }
    ),
)
```
