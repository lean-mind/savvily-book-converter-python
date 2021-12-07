FROM pandoc/latex:latest

# Install latex libraries
RUN tlmgr update --self && tlmgr install emptypage && tlmgr install footmisc && tlmgr install titlesec && tlmgr install wallpaper && tlmgr install roboto && tlmgr install incgraph && tlmgr install tcolorbox && tlmgr install environ
RUN apk add --no-cache poppler-utils

# Install JetBrains Mono font
RUN mkdir -p /usr/share/fonts/
COPY ./JetBrains_Mono/static/*.ttf /usr/share/fonts/
RUN fc-cache -f && rm -rf /var/cache/*
