#!/bin/bash
POSTS_DIR="e:/Repository/geeknite.github.io/_posts"
for file in $(ls "$POSTS_DIR/" | grep -vE "^[0-9]{4}-[0-9]{2}-[0-9]{2}-"); do
    fp="$POSTS_DIR/$file"
    if [ -d "$fp" ]; then continue; fi
    t=$(grep -c "^title:" "$fp" 2>/dev/null || echo 0)
    d=$(grep -c "^date:" "$fp" 2>/dev/null || echo 0)
    g=$(grep -c "^tags:" "$fp" 2>/dev/null || echo 0)
    desc=$(grep -c "^description:" "$fp" 2>/dev/null || echo 0)
    hero=$(grep -c "align-right" "$fp" 2>/dev/null || echo 0)
    aff=$(grep -c "site.constants.wsib" "$fp" 2>/dev/null || echo 0)
    aff2=$(grep -c "geeknite.com" "$fp" 2>/dev/null || echo 0)
    il=$(grep -c "post_url" "$fp" 2>/dev/null || echo 0)
    tbl=$(grep -c "include amazon.html" "$fp" 2>/dev/null || echo 0)
    wc=$(wc -w < "$fp" 2>/dev/null || echo 0)
    echo "$file|$t|$d|$g|$desc|$hero|$aff|$aff2|$il|$tbl|$wc"
done
