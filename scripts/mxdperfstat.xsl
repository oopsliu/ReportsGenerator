<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:output method="html" />

   <xsl:template match="/root/test">
      <html>
         <head>
<style type="text/css">
            body {background-color: transparent}
            h1 {color: purple; background-color: transparent}
            h2 {color: purple; background-color: transparent}
            p {color: purple background-color: transparent}
            
<!--            TABLE  { background: azure; empty-cells: show } -->



            TR.top { background: red }
            TD { }
        
</style>

            <title>mxdperfstat</title>
         </head>

         <body>
            <h1>mxdperfstat</h1>

            <p style="color:purple">
            <xsl:value-of select="@date" />

            <br>
            
            </br>

            <xsl:value-of select="@mxd" />
            <br>
            </br>
            
            layerCount=
            <xsl:value-of select="@layerCount" />

            <br>
            </br>

            <xsl:value-of select="@spatialReferenceName" />

            <br>
            </br>

            <xsl:value-of select="@mapUnits" />

            <br>
            </br>

            X= 
            <xsl:value-of select="@x" />

            Y= 
            <xsl:value-of select="@y" />
            width=
            <xsl:value-of select="@width" />

            height=
            <xsl:value-of select="@height" />
            
            </p>

            <hr>
            </hr>

            <table border="1">
               <caption>
                  <b>Map Display Performance (sec) for each scale</b>
               </caption>

               <tr bgcolor="#ADD8E6">
                  <th>Scale</th>

                  <th>Refresh Time(sec)</th>
                  <th>VisibleLayers</th>
                  
               </tr>

               <xsl:for-each select="//scale">
                 <xsl:sort order="ascending" select="@Scale" data-type="number" />
                 
                 

                  <tr>
                     <td align="right">
                        <xsl:value-of select="@Scale" />
                     </td>

                     <xsl:choose>
                        <xsl:when test="translate(@ScaleRefreshTime, ',','.') &gt; 3">
                           <td align="right" bgcolor="#DC143C">
                              <xsl:value-of select="@ScaleRefreshTime" />
                           </td>
                        </xsl:when>

                        <xsl:otherwise>
                           <td align="right">
                              <xsl:value-of select="@ScaleRefreshTime" />
                           </td>
                        </xsl:otherwise>
                     </xsl:choose>
                     <td align="right">
                        <xsl:value-of select="@VisibleLayerCount" />
                     </td>
                  </tr>
               </xsl:for-each>
            </table>

            <h2>
               <br>
               </br>
            </h2>

            <table border="1">
               <caption>
                  <b>Layer Properties</b>
               </caption>

               <tr bgcolor="#ADD8E6">
                  <th>Item</th>
                 <th>At Scale</th>
                  <th>Layer Name</th>
                  <th>Refresh Time (sec)</th>

                  <th>Recommendations</th>

                  <th>Features</th>

                  <th>Vertices</th>

                  <th>Labeling</th>

                  <th>Geography Phase (sec)</th>

                  <th>Graphics Phase (sec)</th>

                  <th>Cursor Phase (sec)</th>

                  <th>DBMS CPU</th>

                  <th>DBMS LIO</th>

                  <th>DBMS PIO</th>

                  <th>Source</th>

                  <th>LayerType</th>
                  <th>Layer Spatial Reference</th>
                  <th>LayerQueryDef</th>
               </tr>

               <xsl:for-each select="//layer">
                 <!--     <xsl:sort order="descending" select="@LayerRefreshTime" data-type="number" /> -->
                 <xsl:sort order="ascending" select="@AtScale" data-type="number" />

                  <xsl:if test="translate(@LayerRefreshTime, ',', '.') &gt; 0">
                  
                     <tr>
                        <td align="right">
                           <xsl:value-of select="position()" />
                        </td>
                       
                       <td align="right">
                         <xsl:value-of select="@AtScale" />
                       </td>

                        <td width="50">
                           <xsl:value-of select="@LayerName" />
                        </td>

                        <xsl:choose>
                           <xsl:when test="translate(@LayerRefreshTime, ',', '.') &gt; 1">
                              <td align="right" bgcolor="#DC143C">
                                 <xsl:value-of select="@LayerRefreshTime" />
                              </td>

                              <xsl:choose>
                                 <xsl:when test='@Comments=""'>
                                    <td> </td>
                                 </xsl:when>

                                 <xsl:otherwise>
                                    <td align="left" bgcolor="yellow">
                                       <xsl:value-of select="@Comments" />
                                    </td>
                                 </xsl:otherwise>
                              </xsl:choose>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="right">
                                 <xsl:value-of select="@LayerRefreshTime" />
                              </td>

                              <xsl:choose>
                                 <xsl:when test='@Comments=""'>
                                    <td> </td>
                                 </xsl:when>

                                 <xsl:otherwise>
                                    <td align="left">
                                       <xsl:value-of select="@Comments" />
                                    </td>
                                 </xsl:otherwise>
                              </xsl:choose>
                           </xsl:otherwise>
                        </xsl:choose>

                        <xsl:choose>
                           <xsl:when test='@LayerFeatures=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="right">
                                 <xsl:value-of select="@LayerFeatures" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>

                        <xsl:choose>
                           <xsl:when test='@LayerVertices=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="right">
                                 <xsl:value-of select="@LayerVertices" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>

                        <xsl:choose>
                           <xsl:when test='@LayerLabeling=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td>
                                 <xsl:value-of select="@LayerLabeling" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>

                        <td WIDTH="50" align="right">
                           <xsl:value-of select="@LayerTViewGeography" />
                        </td>

                        <td WIDTH="50" align="right">
                           <xsl:value-of select="@LayerTViewGraphics" />
                        </td>

                        <xsl:choose>
                           <xsl:when test='@LayerFCursorTime=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="right">
                                 <xsl:value-of select="@LayerFCursorTime" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>

                        <xsl:choose>
                           <xsl:when test='@LayerCPU=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="right">
                                 <xsl:value-of select="@LayerCPU" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>

                        <xsl:choose>
                           <xsl:when test='@LayerLIO=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="right">
                                 <xsl:value-of select="@LayerLIO" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>

                        <xsl:choose>
                           <xsl:when test='@LayerPIO=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="right">
                                 <xsl:value-of select="@LayerPIO" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>

                        <xsl:choose>
                           <xsl:when test='@LayerPath=""'>
                              <td> </td>
                           </xsl:when>

                           <xsl:otherwise>
                              <td align="left">
                                 <xsl:value-of select="@LayerPath" />
                              </td>
                           </xsl:otherwise>
                        </xsl:choose>
                       <td align="left">
                         <xsl:value-of select="@LayerType" />
                       </td>
                       <td align="left">
                         <xsl:value-of select="@LayerSpatialReferenceName" />
                       </td>
                       <td align="left">
                         <xsl:value-of select="@LayerQueryDef" />
                       </td>
                     </tr>
                  </xsl:if>
               </xsl:for-each>
            </table>

            <h2>
               <br>
               </br>
            </h2>


         </body>
      </html>
   </xsl:template>
</xsl:stylesheet>

