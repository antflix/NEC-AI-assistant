from bs4 import BeautifulSoup
import json

# Sample HTML content
html_content = """<table class="u-mt-1">
<thead>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border uc_top_border_double" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#358" data-next-click="true" data-next-mouseover="true">Article 358</a> - Electrical Metallic Tubing (EMT)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.122</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">118</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.182</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">104</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.161</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">61</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.094</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">15.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.622</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">196</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.304</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">137</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.213</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">206</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.320</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">182</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.283</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">106</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.165</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">20.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.824</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">343</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.533</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">222</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.346</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">333</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.519</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">295</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.458</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">172</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.268</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">26.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.049</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">556</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.864</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">387</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.598</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">581</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.897</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.793</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">300</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.464</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.380</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">968</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.496</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">526</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.814</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">788</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.221</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">696</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.079</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">407</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.631</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">40.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.610</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1314</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.036</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">866</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.342</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1299</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.013</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1147</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.778</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">671</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.040</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">52.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.067</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2165</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.356</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.343</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2270</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.515</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2005</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.105</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1173</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.816</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">69.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.731</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3783</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.858</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2280</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.538</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3421</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.307</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3022</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.688</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1767</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.742</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">85.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.356</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5701</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.846</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2980</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.618</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4471</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.927</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3949</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.119</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2310</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.579</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">97.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.834</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7451</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">11.545</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3808</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.901</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5712</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.852</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5046</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.819</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2951</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.573</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#110.1" data-next-click="true" data-next-mouseover="true">110.1</a></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.334</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">9521</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">14.753</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5220</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.085</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7830</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.127</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6916</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">10.713</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4045</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.266</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">128.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.073</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">13050</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">20.212</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">7528</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">11.663</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">11292</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">17.495</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9975</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">15.454</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">5834</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9.039</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">154.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6.093</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">18821</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">29.158</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#362" data-next-click="true" data-next-mouseover="true">Article 362</a> - Electrical Non-Metallic Tubing (ENT)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">73</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.114</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">110</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.171</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">97</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.151</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">57</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.088</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">15.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.602</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">184</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.285</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">131</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.203</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">197</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.305</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">174</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.269</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">102</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.157</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">20.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.804</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">328</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.508</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">215</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.333</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">322</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.499</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">284</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.441</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">166</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.258</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">26.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.029</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">537</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.832</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">375</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.581</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">562</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.872</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">497</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.770</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">291</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.450</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">34.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.36</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">937</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.453</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">512</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.794</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">769</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.191</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">679</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.052</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">397</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.616</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">40.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.59</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1281</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.986</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">849</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.316</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1274</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.975</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1125</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.744</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">658</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.020</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">52</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.047</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2123</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.291</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#348" data-next-click="true" data-next-mouseover="true">Article 348</a> - Flexible Metal Conduit (FMC)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">30</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.046</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">44</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.069</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">39</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.061</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">23</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.036</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">9.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.384</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">74</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.116</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">81</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.127</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">122</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.190</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.168</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.098</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.635</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">204</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.317</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">137</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.213</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">206</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.320</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">182</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.283</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">106</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.165</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">20.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.824</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">343</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.533</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">211</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.327</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">316</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.490</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">279</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.433</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">163</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.253</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">25.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.020</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">527</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.817</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">330</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.511</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">495</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.766</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">437</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.677</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">256</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.396</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">32.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.275</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">824</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.277</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">480</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.743</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">720</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.115</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">636</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.985</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">372</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.576</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">39.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.538</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1201</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.858</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">843</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.307</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1264</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.961</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1117</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.732</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">653</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.013</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">51.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.040</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2107</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.269</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1267</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.963</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1900</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.945</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1678</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.602</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">982</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.522</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.500</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3167</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.909</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1824</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.827</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2736</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.241</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2417</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.746</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1414</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.191</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">76.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.000</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4560</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.069</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2483</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.848</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3724</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.773</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3290</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.099</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1924</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.983</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">88.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.500</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6207</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">9.621</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">3243</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">5.027</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">4864</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">7.540</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">4297</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6.660</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">3.896</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">101.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">4.000</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">8107</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">12.566</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#342" data-next-click="true" data-next-mouseover="true">Article 342</a> - Intermediate Metal Conduit (IMC)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">89</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.137</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">133</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.205</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">117</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.181</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">69</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.106</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.660</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">222</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.342</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">151</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.235</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">226</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.352</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">200</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.311</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">117</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.182</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.864</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">377</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.586</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">248</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.384</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">372</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.575</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">329</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.508</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">192</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.297</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">28.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.105</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">620</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.959</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">425</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.659</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">638</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.988</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">564</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.873</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">330</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.510</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">36.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.448</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1064</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.647</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">573</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.890</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">859</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.335</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">759</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.179</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">444</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.690</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">42.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.683</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1432</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.225</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">937</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.452</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1405</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.178</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1241</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.924</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">726</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.125</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">54.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.150</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2341</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.630</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1323</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.054</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1985</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.081</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1753</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.722</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1026</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.592</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">64.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.557</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3308</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.135</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2046</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.169</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3069</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.753</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2711</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.199</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1586</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.456</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">80.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.176</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5115</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.922</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2729</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.234</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4093</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.351</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3616</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.610</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2115</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.281</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">93.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.671</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6822</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">10.584</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3490</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.452</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5235</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.179</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4624</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.224</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2705</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.226</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">105.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.166</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8725</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">13.631</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5455</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.528</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8183</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.792</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7229</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">11.30</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4228</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.610</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">131.78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.210</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">13639</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21.32</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">7878</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">12.304</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">11817</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">18.456</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">10439</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">16.302</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6106</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9.536</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">158.36</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6.258</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">19696</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">30.76</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#356" data-next-click="true" data-next-mouseover="true">Article 356</a> - Liquidtight Flexible Nonmetallic Conduit (LFNC-A*)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">50</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.077</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">75</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.115</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">66</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.102</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">39</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.060</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.495</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">125</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.192</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">80</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.125</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">121</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.187</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">107</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.165</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">62</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.097</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.630</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">201</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.312</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">139</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.214</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">208</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.321</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">184</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.283</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">107</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.166</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.825</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">346</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.535</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">221</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.342</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">331</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">292</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.453</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">171</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.265</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">26.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.043</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">552</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.854</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">l<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">387</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.601</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">581</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.901</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.796</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">300</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.466</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.383</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">968</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.502</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">520</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.807</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">781</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.211</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">690</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.070</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">403</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.626</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">40.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.603</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1301</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.018</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">863</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.337</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1294</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2.006</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1143</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.772</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">669</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.036</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">52.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2.063</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2157</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">3.343</td>
</tr>
<tr>
<td class="u-text-12px" colspan="14">*Corresponds to 356.2(1).</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#356" data-next-click="true" data-next-mouseover="true">Article 356</a> - Liquidtight Flexible Nonmetallic Conduit (LFNC-B*)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">49</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.077</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">74</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.115</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">65</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.102</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">38</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.059</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.494</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">123</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.192</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">81</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.125</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">122</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.188</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.166</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.097</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.632</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">204</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.314</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">140</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.216</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">210</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.325</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">185</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.287</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.168</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.830</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">350</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.541</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">226</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.349</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">338</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.524</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">299</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.462</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">175</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.270</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">26.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.054</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">564</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.873</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">394</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.611</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">591</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.917</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">522</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.810</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">305</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.474</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.395</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">984</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.528</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">510</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.792</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">765</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.188</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">676</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.050</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">395</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.614</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">40.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.588</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1276</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.981</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">836</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.298</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1255</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.948</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.720</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">648</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.006</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">51.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2.033</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2091</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">3.246</td>
</tr>
<tr>
<td class="u-text-12px" colspan="14">*Corresponds to 356.2(2).</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#356" data-next-click="true" data-next-mouseover="true">Article 356</a> - Liquidtight Flexible Nonmetallic Conduit (LFNC-C*)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">47.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.074</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">71.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.111</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.098</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">36.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.057</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.485</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">119.19</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.185</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">77.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.121</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">116.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.181</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.160</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">60.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.094</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">15.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.620</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">194.778</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.302</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">134.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.209</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">201.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.313</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">178.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.276</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">104.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.162</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">20.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.815</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">336.568</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.522</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">215.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.333</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">322.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.500</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">284.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.442</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">166.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.258</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">26.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.030</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">537.566</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.833</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">380.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.590</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">570.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.884</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/5/special-occupancies#504.1" data-next-click="true" data-next-mouseover="true">504.1</a></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.781</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">294.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.457</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">34.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.370</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">951.039</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.474</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">509.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.789</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">763.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.184</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">674.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.046</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">394.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.612</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">40.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.585</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1272.963</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.973</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">847.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.314</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1271.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.971</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1123.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.741</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">656.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">1.018</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">51.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2.045</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">2119.063</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">3.285</td>
</tr>
<tr>
<td class="u-text-12px" colspan="14">*Corresponds to 356.2(3).</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#350" data-next-click="true" data-next-mouseover="true">Article 350</a> - Liquidtight Flexible Metal Conduit (LFMC)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">49</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.077</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">74</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.115</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">65</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.102</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">38</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.059</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.494</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">123</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.192</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">81</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.125</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">122</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.188</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.166</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.097</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.632</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">204</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.314</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">140</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.216</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">210</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.325</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">185</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.287</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.168</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.830</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">350</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.541</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">226</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.349</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">338</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.524</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">299</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.462</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">175</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.270</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">26.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.054</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">564</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.873</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">394</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.611</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">591</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.917</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">522</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.810</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">305</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.474</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.395</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">984</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.528</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">510</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.792</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">765</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.188</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">676</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.050</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">395</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.614</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">40.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.588</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1276</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.981</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">836</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.298</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1255</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.948</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.720</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">648</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.006</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">51.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.033</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2091</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.246</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1259</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.953</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1888</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.929</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1668</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.587</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">976</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.493</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3147</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.881</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1931</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.990</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2896</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.485</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2559</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.962</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1497</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.317</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.085</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4827</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.475</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2511</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.893</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3766</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.839</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3327</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.158</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1946</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.017</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">89.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.520</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6277</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">9.731</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3275</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.077</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4912</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.615</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4339</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.727</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2538</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.935</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">102.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.020</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8187</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.692</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#344" data-next-click="true" data-next-mouseover="true">Article 344</a> - Rigid Metal Conduit (RMC)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">81</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.125</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">122</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.188</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">108</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.166</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.097</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.632</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">204</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.314</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">141</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.220</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">212</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.329</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">187</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.291</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">109</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.170</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.836</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">353</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.549</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">229</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.355</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">344</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.532</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">303</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.470</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">177</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.275</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.063</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">573</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.887</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">394</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.610</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">591</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.916</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">522</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.809</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">305</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.473</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.394</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">984</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.526</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">533</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.829</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">800</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.243</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">707</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.098</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">413</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.642</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.624</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1333</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.071</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">879</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.363</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1319</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.045</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1165</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.806</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">681</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.056</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">52.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.083</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2198</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.408</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1255</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.946</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1882</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.919</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1663</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.579</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">972</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.508</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.489</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3137</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.866</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1936</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.000</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2904</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.499</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2565</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.974</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1500</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.325</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.090</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4840</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.499</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2584</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.004</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3877</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.006</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3424</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.305</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2003</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">90.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.570</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6461</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">10.010</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3326</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.153</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4990</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.729</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4408</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.828</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2578</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.994</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">102.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.050</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8316</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.882</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5220</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.085</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7830</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.127</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6916</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">10.713</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4045</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.266</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">128.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.073</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">13050</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">20.212</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">7528</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">11.663</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">11292</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">17.495</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9975</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">15.454</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">5834</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9.039</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">154.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6.093</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">18821</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">29.158</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#352" data-next-click="true" data-next-mouseover="true">Article 352</a> - Rigid PVC Conduit (PVC), Schedule 80</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">56</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.087</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">85</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.130</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">75</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.115</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">44</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.067</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">13.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.526</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">141</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.217</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">105</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.164</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">158</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.246</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">139</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.217</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">82</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.127</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">18.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.722</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">263</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.409</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">178</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.275</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">267</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.413</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">236</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.365</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">138</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.213</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">23.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.936</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">445</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.688</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">320</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.495</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">480</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.742</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">424</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.656</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">248</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.383</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">31.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.255</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">799</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.237</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">442</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.684</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">663</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.027</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">585</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.907</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">342</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.530</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">37.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.476</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1104</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.711</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">742</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.150</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1113</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.725</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">983</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.523</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">575</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.891</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">48.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.913</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1855</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.874</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1064</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.647</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1596</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.471</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1410</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.183</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">825</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.277</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">58.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.290</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2660</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.119</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1660</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.577</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2491</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.865</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2200</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.414</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1287</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.997</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">72.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.864</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4151</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.442</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2243</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.475</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3365</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.213</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2972</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.605</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1738</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.693</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">84.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.326</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5608</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.688</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2907</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.503</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4361</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.755</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3852</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.967</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2253</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.490</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">96.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.786</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7268</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">11.258</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4607</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.142</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6911</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">10.713</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6105</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">9.463</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3571</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.535</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">121.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.768</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">11518</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">17.855</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6605</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">10.239</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9908</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">15.359</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">8752</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">13.567</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">5119</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">7.935</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">145.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">5.709</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">16513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">25.598</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong>Articles <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#352" data-next-click="true" data-next-mouseover="true">352</a> and <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#353" data-next-click="true" data-next-mouseover="true">353</a> - Rigid PVC Conduit (PVC), Schedule 40, and HDPE Conduit (HDPE)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>8</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">74</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.114</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">110</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.171</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">97</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.151</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">57</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.088</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">15.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.602</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">184</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.285</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">131</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.203</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">196</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.305</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">173</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.269</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">101</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.157</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">20.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.804</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">327</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.508</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">214</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.333</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">321</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.499</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">284</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.441</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">166</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.258</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">26.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.029</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">535</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.832</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">374</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.581</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">561</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.872</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">495</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.770</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">290</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.450</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">34.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.360</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">935</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.453</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">513</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.794</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">769</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.191</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">679</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.052</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">397</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.616</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">40.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.590</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1282</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.986</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">849</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.316</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1274</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.975</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1126</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.744</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">658</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.020</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">52.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.047</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2124</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.291</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1212</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.878</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1817</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.817</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1605</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.488</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">939</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.455</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">62.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.445</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3029</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.695</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1877</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.907</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2816</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.361</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2487</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.852</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1455</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.253</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">77.3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.042</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4693</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.268</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2511</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.895</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3766</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.842</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3327</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.161</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1946</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.018</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">89.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.521</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6277</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">9.737</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3237</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.022</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4855</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.532</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4288</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.654</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2508</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.892</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">101.5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.998</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8091</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12.554</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5099</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.904</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7649</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">11.856</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6756</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">10.473</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3952</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.126</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">127.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.016</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">12748</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">19.761</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">7373</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">11.427</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">11060</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">17.140</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9770</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">15.141</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">5714</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">8.856</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">153.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6.031</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">18433</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">28.567</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#352" data-next-click="true" data-next-mouseover="true">Article 352</a> - Type A, Rigid PVC Conduit (PVC)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">100</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.154</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">149</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.231</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">132</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.204</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">77</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.119</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">17.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.700</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">249</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.385</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">168</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.260</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">251</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.390</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">222</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.345</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">130</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.202</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">23.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.910</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">419</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.650</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">279</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.434</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">418</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.651</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">370</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.575</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">216</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.336</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">29.8</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.175</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">697</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.084</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">456</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.707</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">684</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.060</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">604</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.937</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">353</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.548</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">38.1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.500</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1140</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.767</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">600</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.929</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">900</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.394</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">795</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.231</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">465</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">0.720</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">43.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.720</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1500</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.324</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">940</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.459</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1410</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.188</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1245</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.933</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">728</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.131</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">54.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2350</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.647</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1406</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.181</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2109</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.272</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1863</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.890</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1090</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.690</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">66.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.635</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3515</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.453</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2112</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.278</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3169</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.916</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2799</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.343</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1637</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.540</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">82.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.230</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5281</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.194</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2758</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.278</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4137</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.416</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3655</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.668</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2138</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.315</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">93.7</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.690</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6896</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">10.694</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3543</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.489</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5315</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.234</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4695</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.273</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2746</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.254</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">106.2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.180</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8858</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">13.723</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">-</td>
</tr>
<tr>
<th class="u-align-bottom u-pt-4 uc_bottom_border" colspan="14"><strong><a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/3/wiring-methods-and-materials#352" data-next-click="true" data-next-mouseover="true">Article 352</a> - Type EB, Rigid PVC Conduit (PVC)</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Metric Designator</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" rowspan="2"><strong>Trade Size</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Over 2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 40%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>60%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>1 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wire</a> 53%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>2 <a class="autolink" href="/viewer/texas/nfpa-70-2023/chapter/1/general#wire" data-next-click="true" data-next-mouseover="true">Wires</a> 31%</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Nominal Internal Diameter</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border" colspan="2"><strong>Total Area 100%</strong></th>
</tr>
<tr>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.</strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>mm<sup>2</sup></strong></th>
<th class="u-align-bottom u-pl-4 u-pr-4 uc_bottom_border"><strong>in.<sup>2</sup></strong></th>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">16</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">21</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center"><sup>3</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">27</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">35</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>4</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">41</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">53</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">999</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.550</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1499</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.325</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1324</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.053</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">774</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1.201</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">56.4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.221</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2498</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.874</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">63</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">-</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">78</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2248</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.484</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3373</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.226</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2979</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.616</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">1743</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2.700</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">84.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.330</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5621</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.709</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">91</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3<sup>1</sup>/<sub>2</sub></td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2932</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.546</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4397</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.819</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3884</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.023</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2272</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.523</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">96.6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3.804</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7329</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">11.365</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">103</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">3726</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.779</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5589</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.669</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4937</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7.657</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">2887</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.479</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">108.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4.289</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">9314</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">14.448</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">129</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5726</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8.878</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">8588</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">13.317</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">7586</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">11.763</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">4437</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">6.881</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">135.0</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">5.316</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">14314</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center">22.195</td>
</tr>
<tr>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">155</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">8133</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">12.612</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">12200</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">18.918</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">10776</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">16.711</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6303</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">9.774</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">160.9</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">6.336</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">20333</td>
<td class="u-align-top u-pl-4 u-pr-4 u-text-center uc_bottom_border_medium_thick">31.530</td>
</tr>
</tbody>
</table>"""
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize dictionary to hold the tables
tables_dict = {}

# Find all rows in the table
rows = soup.find_all('tr')
current_rows = []
key = None

# Iterate over each row
for i, row in enumerate(rows):
    if row.find('th', class_='u-pt-4'):  # Start of a new table
        if current_rows:
            # Create a new BeautifulSoup table to hold this subset of rows
            new_table = BeautifulSoup('<table></table>', 'html.parser').table
            for r in current_rows:
                new_table.append(r)
            # Store the table in the dictionary using the key
            tables_dict[key] = str(new_table).replace('"', '\\"')  # Minifying and escaping quotes
        # Reset current rows and update the key
        current_rows = [row]
        key = row.th.get_text(strip=True, separator=" ")
    else:
        current_rows.append(row)

# Store the last table
if current_rows and key:
    new_table = BeautifulSoup('<table></table>', 'html.parser').table
    for r in current_rows:
        new_table.append(r)
    tables_dict[key] = str(new_table).replace('"', '\\"')

# Output to a JSON file
with open('table4.json', 'w') as outfile:
    json.dump(tables_dict, outfile, indent=4, ensure_ascii=False)

print("Tables extracted and saved to 'extracted_tables.json'")