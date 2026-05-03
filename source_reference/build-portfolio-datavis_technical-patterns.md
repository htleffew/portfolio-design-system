# Portfolio Technical Patterns 

This file contains the exact blueprint elements that must be copied without alteration by the Data Visualization Engineer.

## The Diverging Bar Chart Fragment (Comparison)
```html
<div class="diverging-chart">
  <div class="diverging-row">
    <div class="diverging-label-left">[LABEL A]</div>
    <div>
      <div class="diverging-bars-left">
        <div class="diverging-bar-left" data-width="[PERCENT]%" style="width: 0;">
          <span class="diverging-val">[PERCENT]%</span>
        </div>
      </div>
    </div>
    <div class="diverging-center">[METRIC NAME]</div>
    <div>
      <div class="diverging-bars-right">
        <div class="diverging-bar-right" data-width="[PERCENT]%" style="width: 0;">
          <span class="diverging-val">[PERCENT]%</span>
        </div>
      </div>
    </div>
    <div class="diverging-label-right">[LABEL B]</div>
  </div>
</div>
```

## The Telemetry Table Fragment (Detailed Data)
```html
<div class="telem-wrap">
  <div class="telem-head">
    <span class="telem-head-label">[TABLE TITLE]</span>
    <div class="telem-toggle">
      <button class="telem-btn active" data-view="full">Full</button>
      <button class="telem-btn" data-view="sig">Significance</button>
    </div>
  </div>
  <div class="telem-descriptives">
    <div class="telem-d-block">
      <div class="telem-d-label">[VAR NAME]</div>
      <div class="telem-d-val">[VAR VALUE]</div>
    </div>
  </div>
  <table class="telem">
    <thead>
      <tr>
        <th style="text-align:left">[COL 1]</th>
        <th>[COL 2]</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align:left">[ROW LABEL]</td>
        <td><span class="[sig-hi OR sig-md]">[VALUE]</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

## The Word Cloud Fragment (Frequency)
```html
<div class="cloud-filters">
  <button class="telem-btn active" data-cat="all">All</button>
  <button class="telem-btn" data-cat="[CATEGORY_KEY]">[CATEGORY NAME]</button>
</div>
<div class="cloud-wrap" id="cloudWrap">
  <!-- LOOP WORDS -->
  <span class="cw" style="font-size: clamp([MIN]px, [SCALE]vw, [MAX]px);" data-cat="[CATEGORY_KEY]">
    [WORD]
    <span class="ftag">n=[COUNT]</span>
  </span>
</div>
```

## The Stat Cards Group
```html
<div class="stats-row">
  <!-- LOOP CARDS -->
  <div class="stat-card">
    <div class="stat-val" data-target="[NUMBER_IF_ANIMATED]">[NUMBER]</div>
    <div class="stat-lbl">[LABEL]</div>
  </div>
</div>
```
