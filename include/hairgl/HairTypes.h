#ifndef HAIRGL_HAIRTYPES_H
#define HAIRGL_HAIRTYPES_H

#include <stdint.h>
#include <hairgl/Math.h>

namespace HairGL
{
    struct HairAssetDescriptor
    {
        uint32_t segmentsCount;
        uint32_t guidesCount;
        Vector4* positions;
    };

    struct HairInstanceSettings
    {
        //GLOBAL
        bool visualizeGuides;
        bool visualizeGrowthMesh;
        bool renderHair;
        Matrix4 modelMatrix;
        float tesselationFactor;
        float density;

        //SHAPE
        float rootWidth;
        float tipWidth;
        float thinningStart;

        //MATERIAL
        float specular;
        float diffuse;
        float ambient;
        float specularPower;
        Vector4 color;

        //SIMULATION
        float windMagnitude;
        float globalStiffness;
		float localStiffness;
        float damping;
		Vector3 wind;
        float thetaX;
        float thetaY;
        float thetaZ;
        float ks;
        float kb;
        float kt;

        HairInstanceSettings() :
            visualizeGuides(false),
            visualizeGrowthMesh(false),
            renderHair(true),
            tesselationFactor(1.0f),
            density(16.0f),
            rootWidth(0.001f),
            tipWidth(0.0005f),
            thinningStart(0.5f),
            specular(0.5f),
            diffuse(0.5f),
            ambient(0.5f),
            specularPower(50.0f),
            color(0, 0, 0, 1),
            globalStiffness(0),
			localStiffness(0),
            damping(0.3),
			wind(0, 0, 0),
            windMagnitude(0.0f),
            thetaX(0),
            thetaY(0),
            thetaZ(0),
            ks(50000),
            kb(0),
            kt(0)
        {
            modelMatrix.SetIdentity();
        }
    };
}

#endif