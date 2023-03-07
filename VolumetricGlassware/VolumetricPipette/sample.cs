//----------------------
// <auto-generated>
//     Generated using the NJsonSchema v10.8.0.0 (Newtonsoft.Json v13.0.1.0) (http://NJsonSchema.org)
// </auto-generated>
//----------------------


namespace MyNamespace
{
    #pragma warning disable // Disable all warnings

    /// <summary>
    /// ホールピペット(JIS R 3505 / ISO 1769) json schema
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCode("NJsonSchema", "10.8.0.0 (Newtonsoft.Json v13.0.1.0)")]
    public partial class Sample
    {
        /// <summary>
        /// VolumetricPippet
        /// </summary>
        [Newtonsoft.Json.JsonProperty("VolumetricPipette", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public System.Collections.Generic.ICollection<VolumetricPipette> VolumetricPipette { get; set; }



        private System.Collections.Generic.IDictionary<string, object> _additionalProperties;

        [Newtonsoft.Json.JsonExtensionData]
        public System.Collections.Generic.IDictionary<string, object> AdditionalProperties
        {
            get { return _additionalProperties ?? (_additionalProperties = new System.Collections.Generic.Dictionary<string, object>()); }
            set { _additionalProperties = value; }
        }

    }

    [System.CodeDom.Compiler.GeneratedCode("NJsonSchema", "10.8.0.0 (Newtonsoft.Json v13.0.1.0)")]
    public partial class VolumetricPipette
    {
        /// <summary>
        /// ホールピペットの容量
        /// </summary>
        [Newtonsoft.Json.JsonProperty("NominalCapacity", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public double NominalCapacity { get; set; }

        /// <summary>
        /// ホールピペットの許容誤差
        /// </summary>
        [Newtonsoft.Json.JsonProperty("CapacityTolerance", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        [System.ComponentModel.DataAnnotations.Range(0.005D, 0.2D)]
        public double CapacityTolerance { get; set; }

        /// <summary>
        /// ホールピペットの等級
        /// </summary>
        [Newtonsoft.Json.JsonProperty("Class", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        [Newtonsoft.Json.JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public VolumetricPipetteClass Class { get; set; }

        /// <summary>
        /// ホールピペットの出受の定義
        /// </summary>
        [Newtonsoft.Json.JsonProperty("Calibration", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        [Newtonsoft.Json.JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public VolumetricPipetteCalibration Calibration { get; set; }

        /// <summary>
        /// ホールピペット上部のカラーコード
        /// </summary>
        [Newtonsoft.Json.JsonProperty("ColorCode", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public ColorCode ColorCode { get; set; }



        private System.Collections.Generic.IDictionary<string, object> _additionalProperties;

        [Newtonsoft.Json.JsonExtensionData]
        public System.Collections.Generic.IDictionary<string, object> AdditionalProperties
        {
            get { return _additionalProperties ?? (_additionalProperties = new System.Collections.Generic.Dictionary<string, object>()); }
            set { _additionalProperties = value; }
        }

    }

    [System.CodeDom.Compiler.GeneratedCode("NJsonSchema", "10.8.0.0 (Newtonsoft.Json v13.0.1.0)")]
    public enum VolumetricPipetteClass
    {

        [System.Runtime.Serialization.EnumMember(Value = @"A")]
        A = 0,


        [System.Runtime.Serialization.EnumMember(Value = @"B")]
        B = 1,


        [System.Runtime.Serialization.EnumMember(Value = @"SuperGrade")]
        SuperGrade = 2,


        [System.Runtime.Serialization.EnumMember(Value = @"HighGrade")]
        HighGrade = 3,


    }

    [System.CodeDom.Compiler.GeneratedCode("NJsonSchema", "10.8.0.0 (Newtonsoft.Json v13.0.1.0)")]
    public enum VolumetricPipetteCalibration
    {

        [System.Runtime.Serialization.EnumMember(Value = @"TD")]
        TD = 0,


    }

    [System.CodeDom.Compiler.GeneratedCode("NJsonSchema", "10.8.0.0 (Newtonsoft.Json v13.0.1.0)")]
    public partial class ColorCode
    {
        /// <summary>
        /// ホールピペットのカラーコードの色
        /// </summary>
        [Newtonsoft.Json.JsonProperty("Color", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        [Newtonsoft.Json.JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public ColorCodeColor Color { get; set; }

        /// <summary>
        /// ホールピペットのカラーコードの帯数
        /// </summary>
        [Newtonsoft.Json.JsonProperty("NumberOfRing", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public ColorCodeNumberOfRing NumberOfRing { get; set; }



        private System.Collections.Generic.IDictionary<string, object> _additionalProperties;

        [Newtonsoft.Json.JsonExtensionData]
        public System.Collections.Generic.IDictionary<string, object> AdditionalProperties
        {
            get { return _additionalProperties ?? (_additionalProperties = new System.Collections.Generic.Dictionary<string, object>()); }
            set { _additionalProperties = value; }
        }

    }

    [System.CodeDom.Compiler.GeneratedCode("NJsonSchema", "10.8.0.0 (Newtonsoft.Json v13.0.1.0)")]
    public enum ColorCodeColor
    {

        [System.Runtime.Serialization.EnumMember(Value = @"Blue")]
        Blue = 0,


        [System.Runtime.Serialization.EnumMember(Value = @"White")]
        White = 1,


        [System.Runtime.Serialization.EnumMember(Value = @"Red")]
        Red = 2,


        [System.Runtime.Serialization.EnumMember(Value = @"Green")]
        Green = 3,


        [System.Runtime.Serialization.EnumMember(Value = @"Yellow")]
        Yellow = 4,


        [System.Runtime.Serialization.EnumMember(Value = @"Orange")]
        Orange = 5,


        [System.Runtime.Serialization.EnumMember(Value = @"Black")]
        Black = 6,


    }

    [System.CodeDom.Compiler.GeneratedCode("NJsonSchema", "10.8.0.0 (Newtonsoft.Json v13.0.1.0)")]
    public enum ColorCodeNumberOfRing
    {

        _1 = 1,


        _2 = 2,


    }
}