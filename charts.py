import plotly.graph_objects as go

fig = go.Figure(data=go.Scatterpolar(
  r=[4, 5, 3, 3, 3],
  theta=['SQL', 'Python', 'Git', 'Docker', 'Linux'],
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False
)

fig.show()