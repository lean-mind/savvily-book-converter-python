FROM pandoc/latex:latest
RUN tlmgr update --self && tlmgr install titlesec && tlmgr install wallpaper && tlmgr install roboto && tlmgr install incgraph

RUN apk add --no-cache poppler-utils

COPY ./JetBrains_Mono/static/* /usr/shared/fonts/

# refresh system font cache
RUN fc-cache -f -v

